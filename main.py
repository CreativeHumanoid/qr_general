from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime

app = FastAPI()

# 🔗 Replace with your Apps Script URL
BASE_GSHEET_URL = "https://script.google.com/macros/s/AKfycbxxIjCm7Wkz0_ItghMJYlapbNNlhYxRhHdFbRx7H-LYGYaBHuiWECV_ZjeN-R_0V9QZ/exec"


# 🔁 Background update (increment count)
def update_gsheet(qr_type: str):
    try:
        url = f"{BASE_GSHEET_URL}?action=increment&type={qr_type}"
        requests.get(url, timeout=3)
    except Exception as e:
        print("GSHEET ERROR:", e)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                font-family: sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: #111;
                color: white;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Welcome</h1>
            <p>Santulit Kishan Mahotsav</p>
        </div>
    </body>
    </html>
    """


# 🎯 Scan endpoint
@app.get("/open-entry", response_class=HTMLResponse)
def open_entry(request: Request, background_tasks: BackgroundTasks, type: str = "A"):

    # ⚡ increment in background
    background_tasks.add_task(update_gsheet, type)

    # 🔄 fetch current count
    try:
        url = f"{BASE_GSHEET_URL}?type={type}"
        res = requests.get(url, timeout=2)
        count = res.json().get("count", "N/A")
    except:
        count = "..."

    print(f"Scan | Type: {type} | IP: {request.client.host} | Time: {datetime.now()}")

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                font-family: sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: #16a34a;
                color: white;
                text-align: center;
            }}
            .box {{
                padding: 20px;
            }}
            .icon {{
                font-size: 60px;
            }}
            .title {{
                font-size: 26px;
                font-weight: bold;
            }}
            .count {{
                font-size: 16px;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <div class="icon">✅</div>
            <div class="title">Entry Allowed</div>
            <div>Type: {type}</div>
            <div class="count">Count: {count}</div>
        </div>
    </body>
    </html>
    """
