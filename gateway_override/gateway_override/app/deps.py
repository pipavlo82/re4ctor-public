import os
from fastapi import Header, HTTPException, status

def _allowed_keys() -> set[str]:
    raw = (os.getenv("R4_ALLOWED_KEYS") or "").strip()
    keys = {k.strip() for k in raw.split(",") if k.strip()}
    demo = (os.getenv("DEMO_API_KEY") or "").strip()
    if demo:
        keys.add(demo)
    return keys

_ALLOWED = _allowed_keys()

async def require_api_key(x_api_key: str | None = Header(default=None)):
    k = (x_api_key or "").strip()
    if (not k) or (k not in _ALLOWED):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
