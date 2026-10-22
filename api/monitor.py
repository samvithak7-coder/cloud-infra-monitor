from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/api/monitor', methods=['GET'])
def get_metrics():
    metrics = {
        "status": "healthy",
        "cpu_usage_percent": round(random.uniform(15.0, 45.0), 2),
        "memory_usage_percent": round(random.uniform(30.0, 60.0), 2),
        "latency_ms": round(random.uniform(20.0, 120.0), 2),
        "active_nodes": 4,
        "timestamp": int(time.time())
    }
    return jsonify(metrics)

# Required entry point for Vercel Serverless
if __name__ == '__main__':
    app.run()