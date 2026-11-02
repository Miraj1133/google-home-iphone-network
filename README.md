# Google Home on an iPhone Hotspot

Set up an old Google Home speaker (original Google Home, Home Mini, Nest Mini and similar) so it runs on your **iPhone Personal Hotspot**, with no home Wi-Fi needed.

## Why it normally fails

During setup, the Google Home app must be on the **same Wi-Fi network** as the speaker.
When your iPhone *is* the hotspot, the iPhone isn't joined to that network itself, so the app can't
find the speaker or shows "Couldn't communicate with your Google Home".

The fix is to run the setup from a device that **is** on the hotspot network. You only have to do this
once. After that, the speaker reconnects to your hotspot automatically.

---

## Step 0: Prepare your iPhone hotspot

1. **Settings → Personal Hotspot → Allow Others to Join**: ON
2. **Maximize Compatibility**: ON (iPhone 12 or newer). This switches the hotspot to 2.4 GHz, which old speakers handle best.
3. Use a **simple hotspot name**: Settings → General → About → Name. Avoid emojis and apostrophes (`Saidul's iPhone` → `SaidulPhone`).
4. Use a **simple password** of 8+ letters/numbers, with no special symbols.
5. Keep the hotspot screen open while setting up. iPhone hides the hotspot when the screen locks.

## Step 1: Factory-reset the speaker (if it was set up before)

| Model | How to reset |
|---|---|
| Google Home (original) | Hold the mic-mute button on the back for ~15 s until it says it's resetting |
| Google Home Mini | Hold the reset button under the power cable for ~15 s |
| Nest Mini (2nd gen) | Turn mic switch OFF, then press and hold the centre of the top for ~15 s |

The speaker will say it's ready to be set up.

---

## Method A: Use a second device (recommended)

You need **any** second phone, iPad or tablet (a friend's is fine).

1. Turn on your iPhone hotspot (Step 0).
2. Connect the **second device** to your iPhone hotspot.
3. On the second device, install **Google Home** and sign in with **your** Google account.
4. Turn on Bluetooth and Location (Android) / Local Network access (iPhone: Settings → Google Home → Local Network).
5. Tap **+ → Set up device → New device** and follow the prompts.
6. When asked for Wi-Fi, choose **your iPhone hotspot** and enter its password.
7. Done. You can sign out on the second device; the speaker stays linked to your account.

## Method B: The "same name" trick (no second device needed at setup time)

The speaker only remembers a Wi-Fi **name + password**. If another network has exactly the same
name and password as your hotspot, the speaker can't tell them apart.

1. Note your hotspot **name** and **password** exactly (case-sensitive).
2. Make another network with the **identical** name and password, for example:
   - a friend's phone hotspot, renamed to match yours, or
   - a router you have temporary access to (library, friend's house: needs admin access to rename it).
3. Connect **your iPhone** to that network and set the speaker up on it normally in Google Home.
4. Turn that network off. Turn **your** hotspot on.
5. Within a minute or two the speaker joins your hotspot by itself.

## Method C: Only an iPhone + a Mac (no second phone)

The Mac takes internet from the iPhone over a **USB cable** and broadcasts its own Wi-Fi.
You set the speaker up on the Mac's Wi-Fi, then give your iPhone hotspot the **same name and
password** so the speaker moves over by itself (same idea as Method B).

> Untested combination: it relies on the iPhone sharing internet over USB while it is joined to the
> Mac's Wi-Fi. If Google Home reports "no internet" at step 4, use Method A.

1. **iPhone → Mac by cable.** Turn on Personal Hotspot, plug the iPhone into the Mac, tap **Trust**.
2. **On the Mac:** System Settings → General → Sharing → **ⓘ** next to **Internet Sharing**:
   - Share your connection from: **iPhone USB**
   - To devices using: **Wi-Fi**
   - **Wi-Fi Options…** → Network Name `MirajHome`, Security **WPA2/WPA3 Personal**, Password `miraj12345`
     (any simple name/password works; just remember them exactly)
   - Turn **Internet Sharing** on.
3. **On the iPhone:** Settings → Wi-Fi → join `MirajHome`.
4. Open **Google Home** → **+ → Set up device → New device**, and give the speaker the `MirajHome` Wi-Fi.
5. **Make the hotspot identical:**
   - Settings → General → About → **Name** → `MirajHome`
   - Settings → Personal Hotspot → **Wi-Fi Password** → `miraj12345`
6. Turn off Internet Sharing on the Mac, unplug the cable, turn the iPhone hotspot on
   (**Maximize Compatibility** ON).
7. Wait 1–2 minutes → "Hey Google, what time is it?"

**Quick first try (no Mac needed):** with the hotspot on, run Google Home setup directly on the same
iPhone. It sometimes works with newer app versions; if it ends in "Couldn't communicate", use Method A or C.

---

## Step 2: Check it worked

- Say **"Hey Google, what's the weather?"**. If it answers, it's online through your hotspot.
- On iPhone: Settings → Personal Hotspot shows "1 Connection" (or more).
- Optional, from a laptop joined to the hotspot: run the checker script:

```bash
python3 tools/check_speaker.py            # scans the hotspot network for the speaker
python3 tools/check_speaker.py 172.20.10.3  # or check a known IP
```

It prints the speaker's name, which Wi-Fi it's on and its signal strength. No login needed, and it
changes nothing on the device.

## Daily use

- Turn on your hotspot **before** (or soon after) plugging in the speaker.
- Voice commands, music via "Hey Google, play…" and alarms all work normally.
- **Casting from the same iPhone that runs the hotspot** may or may not appear. If it doesn't, use voice
  commands, or cast from another device joined to the hotspot.
- Streaming music uses mobile data (~1 MB per minute at normal quality). Keep an eye on your plan.

Still stuck? See [docs/troubleshooting.md](docs/troubleshooting.md).

## Repo layout

```
README.md                 this guide
docs/troubleshooting.md   common errors and fixes
tools/check_speaker.py    read-only checker (Python 3, no extra packages)
```

## Disclaimer

Not affiliated with Google. The checker uses the speaker's unofficial, read-only local info endpoint
(`/setup/eureka_info`), which Google could change at any time.
