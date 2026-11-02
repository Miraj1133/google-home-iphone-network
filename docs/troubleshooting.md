# Troubleshooting

| Problem | Fix |
|---|---|
| Hotspot doesn't appear in the Wi-Fi list | Keep iPhone's Personal Hotspot screen open; turn on **Maximize Compatibility**; toggle hotspot off/on. |
| "Couldn't communicate with your Google Home" | The setup device isn't on the same network as the speaker. Use Method A or B. Also check Settings → Google Home → **Local Network** is ON. |
| App can't find the speaker | Turn Bluetooth on; stand within ~3 m; factory-reset the speaker and try again. |
| Wrong password error, but it's correct | Remove special characters/emojis from hotspot name and password, then retry. |
| Set up fine, but goes offline later | iPhone turns hotspot off after a while with no devices. Re-open the Personal Hotspot screen; the speaker reconnects in ~1 minute. |
| Speaker joined, but no voice answers | Check the iPhone has mobile data (try a website on the iPhone). Low-data mode can slow it. |
| Can't cast from the hotspot iPhone | Expected sometimes. Use "Hey Google, play … on Spotify/YouTube Music" or cast from a second device on the hotspot. |
| Method B didn't switch over | The name/password must match **exactly** (capitals, spaces). Unplug and re-plug the speaker after turning your hotspot on. |
| Method C: Mac has no "iPhone USB" option | Unlock the iPhone, tap **Trust**, keep Personal Hotspot on; try another cable. |
| Method C: Wi-Fi option greyed out in Internet Sharing | Pick "iPhone USB" as the source first; the Mac's Wi-Fi must not be the source. |
| Method C: "No internet" during setup | The iPhone can't share over USB while on the Mac's Wi-Fi. Use Method A (borrow a phone for 5 min). |
| "Device not supported" in app | Update the Google Home app. Very old firmware updates itself once it's online. |

## Useful facts

- iPhone hotspot addresses are usually `172.20.10.x` (the iPhone itself is `172.20.10.1`).
- Speakers remember the network by **name + password**, which is why Method B works.
