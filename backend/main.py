from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "TestPilot AI backend is running"}

class ScanRequest(BaseModel):
    url: str

@app.post("/api/scans")
def create_scan(scan: ScanRequest):
    return {
        "message": "Scan received",
        "url": scan.url
    }