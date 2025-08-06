# Bloodmoon Warning

A simple Python script to monitor the in-game time of a **7 Days to Die** server and send Discord alerts for upcoming Blood Moon events.

---

## Features

- Checks your 7 Days to Die server’s game time API.
- Sends a Discord webhook alert **the day before** and **on the day** of a Blood Moon.
- Customizable Blood Moon frequency (default: every 7 days).
- Includes optional alert images to spice up your Discord notifications.

---

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- A 7 Days to Die server exposing the API at `/api/getstats`
- A Discord webhook URL for alerts

---

## Setup

1. Clone or download this repository.
2. Edit `bloodmoon_announcer.py` to set your:
   - `API_URL` (your server IP and port)
   - `DISCORD_WEBHOOK` (your Discord webhook URL)
   - `BLOOD_MOON_FREQ` (optional: days between Blood Moons, default 7)
3. (Optional) Replace alert image URLs in the script or remove them.
4. Run the script:

```bash
python bloodmoon_announcer.py
