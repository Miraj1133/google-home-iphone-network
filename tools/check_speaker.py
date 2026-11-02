#!/usr/bin/env python3
"""Read-only checker: find a Google Home speaker on the current network and
show which Wi-Fi it is connected to.

Usage:
    python3 check_speaker.py              # scan (default: iPhone hotspot range 172.20.10.0/28)
    python3 check_speaker.py 172.20.10.3  # check one IP
    python3 check_speaker.py --subnet 192.168.1.0/24

Uses only the Python standard library. It sends GET requests to the speaker's
unofficial local info endpoint (/setup/eureka_info) and changes nothing.
"""
import argparse
import ipaddress
import json
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

PARAMS = "name,build_info,net,wifi,device_info,setup"
TIMEOUT = 2.0

# The speaker uses a self-signed certificate on 8443. We only read public,
# non-sensitive device info from it, so certificate checks are skipped there.
_INSECURE = ssl.create_default_context()
_INSECURE.check_hostname = False
_INSECURE.verify_mode = ssl.CERT_NONE


def fetch_info(ip):
    """Return device info dict for ip, or None if it isn't a Cast device."""
    urls = [
        (f"http://{ip}:8008/setup/eureka_info?params={PARAMS}&options=detail", None),
        (f"https://{ip}:8443/setup/eureka_info?params={PARAMS}&options=detail", _INSECURE),
    ]
    for url, ctx in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "check_speaker"})
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                data = json.loads(r.read().decode("utf-8", "replace"))
                if isinstance(data, dict) and ("name" in data or "net" in data):
                    return data
        except Exception:
            continue
    return None


def describe(ip, d):
    net = d.get("net", {}) or {}
    wifi = d.get("wifi", {}) or {}
    build = d.get("build_info", {}) or {}
    dev = d.get("device_info", {}) or {}
    ssid = wifi.get("ssid") or net.get("ssid") or "?"
    rssi = wifi.get("signal_level")
    lines = [
        f"Found speaker at {ip}",
        f"  Name:      {d.get('name', '?')}",
        f"  Model:     {dev.get('model_name') or dev.get('product_name') or '?'}",
        f"  Wi-Fi:     {ssid}",
        f"  Online:    {'yes' if net.get('online', True) else 'no'}",
    ]
    if rssi is not None:
        quality = "good" if rssi > -60 else "ok" if rssi > -75 else "weak"
        lines.append(f"  Signal:    {rssi} dBm ({quality})")
    if build.get("cast_build_revision"):
        lines.append(f"  Firmware:  {build['cast_build_revision']}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ip", nargs="?", help="speaker IP to check")
    p.add_argument("--subnet", default="172.20.10.0/28",
                   help="range to scan if no IP given (default: iPhone hotspot)")
    a = p.parse_args()

    if a.ip:
        targets = [a.ip]
    else:
        try:
            net = ipaddress.ip_network(a.subnet, strict=False)
        except ValueError as e:
            sys.exit(f"Bad subnet: {e}")
        if net.num_addresses > 1024:
            sys.exit("Subnet too large; use /22 or smaller.")
        targets = [str(h) for h in net.hosts()]
        print(f"Scanning {len(targets)} addresses in {net} ...")

    with ThreadPoolExecutor(max_workers=64) as ex:
        results = list(zip(targets, ex.map(fetch_info, targets)))

    found = [(ip, d) for ip, d in results if d]
    if not found:
        print("No Google Home found.")
        print("- Is this computer connected to the same hotspot?")
        print("- Is the speaker powered on and set up (see README)?")
        sys.exit(1)
    for ip, d in found:
        print(describe(ip, d))


if __name__ == "__main__":
    main()
