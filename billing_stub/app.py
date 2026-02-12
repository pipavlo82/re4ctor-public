from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="r4-billing-stub", version="0.1.0")

class GateReq(BaseModel):
    api_key: str
    path: str = "/v1/random"
    method: str = "GET"

@app.get("/health")
def health():
    return {"ok": True, "svc": "billing-stub"}

@app.post("/gate/allow")
def gate_allow(req: GateReq):
    k = (req.api_key or "").strip()
    if not k:
        return {"ok": False, "reason": "missing_key"}
    if k == "demo":
        return {
            "ok": True, "plan": "demo", "path": req.path,
            "used_today": 1, "quota_per_day": 200, "rate_limit_rps": 1
        }
    if k.startswith("r4_"):
        return {
            "ok": True, "plan": "paid", "path": req.path,
            "used_today": 1, "quota_per_day": 100000, "rate_limit_rps": 20
        }
    return {"ok": False, "reason": "api_key_not_found"}

@app.post("/webhook/stripe")
def webhook():
    return {"ok": True}
