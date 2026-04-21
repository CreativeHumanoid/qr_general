from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

entry_count = 0


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: #111;
                color: white;
                text-align: center;
            }
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 28px;
                margin-bottom: 10px;
            }
            p {
                font-size: 18px;
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome</h1>
            <p>Santulit Kishan Mahotsav</p>
        </div>
    </body>
    </html>
    """


@app.get("/open-entry", response_class=HTMLResponse)
def open_entry(request: Request):
    global entry_count
    entry_count += 1

    print(f"Entry #{entry_count} | IP: {request.client.host} | Time: {datetime.now()}")

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Entry Allowed</title>
        <style>
            body {{
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #16a34a;
                color: white;
                text-align: center;
            }}
            .card {{
                padding: 30px 20px;
            }}
            .icon {{
                font-size: 60px;
                margin-bottom: 15px;
            }}
            .title {{
                font-size: 28px;
                font-weight: 600;
                margin-bottom: 10px;
            }}
            .count {{
                font-size: 16px;
                opacity: 0.9;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">✅</div>
            <div class="title">Entry Allowed</div>
            <div class="count">Total Entries: {entry_count}</div>
        </div>
    </body>
    </html>
    """
