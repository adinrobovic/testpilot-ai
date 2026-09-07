from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scanner import scan_page

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "TestPilot AI backend is running"}

class ScanRequest(BaseModel):
    url: str

@app.post("/api/scans")
async def create_scan(scan: ScanRequest):
    result = await scan_page(scan.url)

    return result