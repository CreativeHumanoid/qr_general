from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

# Optional: simple in-memory counter
entry_count = 0


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style='font-family:sans-serif;text-align:center;margin-top:20%;'>
    <h1>QR Entry System</h1>
    <p>Scan QR to allow entry</p>
    </body>
    </html>
    """


# 🎯 Universal Entry Endpoint
@app.get("/open-entry", response_class=HTMLResponse)
def open_entry(request: Request):
    global entry_count
    entry_count += 1

    # Log (visible in Render logs)
    print(f"Entry #{entry_count} | IP: {request.client.host} | Time: {datetime.now()}")

    return f"""
    <html>
    <head>
        <title>Entry Allowed</title>
    </head>
    <body style='background-color:green;color:white;text-align:center;margin-top:20%;font-size:40px;font-family:sans-serif;'>
        ✅ Entry Allowed<br><br>
        <span style='font-size:20px;'>Count: {entry_count}</span>
    </body>
    </html>
    """