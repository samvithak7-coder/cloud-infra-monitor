# Cloud Infrastructure & Log Monitor

A serverless dashboard that shows the health of a cloud environment at a glance. It tracks CPU usage, memory usage, request latency and the number of active nodes, and summarizes them in an overall system status badge. The backend is a Python API deployed on Vercel.

**Live demo:** https://cloud-infra-monitor-lyart.vercel.app/

## Overview

The dashboard fetches metrics from a Python serverless endpoint and renders them as live cards. A "Refresh Metrics" button pulls fresh values on demand. The project demonstrates a full request flow from browser to API to UI, deployed with zero server management.

## Features

- Real-time metric cards: CPU usage, memory usage, latency (ms) and active nodes
- Overall system status badge
- On-demand refresh from the API
- Responsive dark-themed interface
- Serverless Python backend deployed on Vercel

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python (Vercel serverless function) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Vercel |
| Version control | Git, GitHub |

## How It Works

1. The browser loads `public/index.html`.
2. `public/script.js` sends a `GET` request to `/api/monitor`.
3. `api/monitor.py` returns the current metrics as JSON.
4. The page updates the metric cards and the status badge.

The metrics are simulated with values in realistic ranges, which keeps the project self-contained while demonstrating the monitoring pipeline.

## API

**`GET /api/monitor`**

Returns the current infrastructure metrics (CPU, memory, latency, active nodes and system status) as JSON.

## Project Structure

```
cloud-infra-monitor/
├── api/
│   └── monitor.py       # Serverless metrics endpoint
├── public/
│   ├── index.html       # Dashboard UI
│   └── script.js        # Fetches and renders metrics
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel routing config
└── README.md
```

## Run Locally

```bash
git clone https://github.com/samvithak7-coder/cloud-infra-monitor.git
cd cloud-infra-monitor
pip install -r requirements.txt
npm install -g vercel
vercel dev
```

Open http://localhost:3000 in your browser.

## Deployment

The project is deployed on Vercel. Every push to the `main` branch triggers an automatic redeploy.

## Future Improvements

- Threshold-based alerts (for example, flag CPU above 80%)
- Auto-refresh with a chart of recent readings
- Persistent storage of readings for historical analysis
- Real system metrics instead of simulated values

## Author

**Samvitha K**
[GitHub](https://github.com/samvithak7-coder) · [LinkedIn](https://www.linkedin.com/in/kesapragada-samvitha-977714376/)
