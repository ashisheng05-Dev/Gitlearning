import requests
import os
import time
import json
from datetime import datetime

url = os.getenv("SITE_URL")
if not url:
    raise SystemExit("SITE_URL must be set to the deployed site URL")

start = time.time()
response = requests.get(url, timeout=30)
latency = (time.time() - start) * 1000  # ms

metrics = {
    "url": url,
    "status": response.status_code,
    "latency_ms": round(latency, 2),
    "content_length": len(response.content),
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

print(json.dumps(metrics, indent=2))

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

if not 200 <= response.status_code < 300:
    raise SystemExit(f"Site health check failed with HTTP {response.status_code}")
