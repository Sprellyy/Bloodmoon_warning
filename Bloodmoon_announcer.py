import requests
import time
import datetime

API_URL = "http://SERVER_IP_GOES HERE/api/getstats" #add server IP here
API_AUTH = None
DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK" #add discord webhook here - see readme file to see how.
BLOOD_MOON_FREQ = 7 #this is the amount of days between bloodmoons on your server
last_alerted_day = None

def send_discord_alert(message, title=None, color=0xff0000, image_url=None):
    embed = {
        "title": title or "Blood Moon Alert",
        "description": message,
        "color": color,
    }
    if image_url:
        embed["image"] = {"url": image_url}

    payload = {
        "embeds": [embed]
    }
    r = requests.post(DISCORD_WEBHOOK, json=payload)
    if r.status_code != 204:
        print(f"[!] Discord error: {r.status_code} - {r.text}")

def check_bloodmoon():
    global last_alerted_day

    try:
        r = requests.get(API_URL, auth=API_AUTH)
        data = r.json()

        days = data["gametime"]["days"]
        hours = data["gametime"]["hours"]
        minutes = data["gametime"]["minutes"]

        current_day = int(days)
        current_hour = int(hours)
        current_minute = int(minutes)

        if current_day % BLOOD_MOON_FREQ == 0:
            next_bloodmoon_day = current_day
        else:
            next_bloodmoon_day = ((current_day // BLOOD_MOON_FREQ) + 1) * BLOOD_MOON_FREQ

        print(f"DEBUG: Day={current_day}, Hour={current_hour}, Next Blood Moon={next_bloodmoon_day}, Last Alerted={last_alerted_day}")

        if current_day == next_bloodmoon_day and current_hour >= 12:
            if last_alerted_day != current_day:
                send_discord_alert(
                    message=f"🌕 **Blood Moon is TONIGHT!!!** (Day {current_day}) (Time {current_hour}:{current_minute:02d})",
                    title="🩸 Blood Moon Day!!!!!",
                    color=0xFF4500,
                    image_url="ADD_IMAGE_HERE" #add whatever image you want here to show on discord.
                )
                last_alerted_day = current_day
        
        elif current_day == (next_bloodmoon_day - 1) and current_hour >= 15:
            if last_alerted_day != current_day + 0.5:
                send_discord_alert(
                    message=f"🔔 **Blood Moon is TOMORROW!** Prepare for Day {next_bloodmoon_day}",
                    title="🩸 Blood Moon Alert",
                    color=0xFFA500,
                    image_url="ADD_IMAGE_HERE" #add whatever image you want here to show on discord.
                )
                last_alerted_day = current_day + 0.5

    except Exception as e:
        print("[!] Error:", e)

def run_monitor():
    print("📡 Monitoring Blood Moon status...")
    while True:
        print(f"⏰ Checking at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        check_bloodmoon()
        time.sleep(60)

if __name__ == "__main__":
    run_monitor()
