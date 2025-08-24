from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import socket
import time
from datetime import datetime

app = FastAPI(
    title="FastAPI ML App",
    description="A FastAPI ML application running on K3s",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoints
@app.get("/")
def root():
    return {
        "message": "FastAPI is running!",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "version": "1.0.0"
    }

@app.get("/ping")
def ping():
    return {"message": "pong", "timestamp": datetime.now().isoformat()}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "uptime": time.time()
    }

@app.get("/info")
def app_info():
    return {
        "app": "FastAPI ML App",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "registry": os.getenv("REGISTRY_URL", "192.168.0.200:5000"),
        "namespace": os.getenv("NAMESPACE", "fastapi-ml"),
        "build_time": datetime.now().isoformat()
    }

# ML-related endpoints (examples)
@app.get("/predict")
def predict():
    """Placeholder for ML prediction endpoint"""
    return {
        "prediction": "sample_prediction",
        "model_version": "1.0.0",
        "confidence": 0.95,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/model/status")
def model_status():
    """Model health and status endpoint"""
    return {
        "model_loaded": True,
        "model_version": "1.0.0",
        "last_updated": datetime.now().isoformat(),
        "status": "ready"
    }

# Kubernetes readiness and liveness probes
@app.get("/ready")
def readiness_probe():
    """Kubernetes readiness probe"""
    return {"status": "ready"}

@app.get("/live")
def liveness_probe():
    """Kubernetes liveness probe"""
    return {"status": "alive"}
