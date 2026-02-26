from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.health import router as health_router

app = FastAPI(title="AppName API")

app.include_router(health_router, prefix="/api")

# Serve static assets (Vite build output copied here)
# In bundled mode, see build playbook for get_static_dir resolution strategy.
if (STATIC_DIR := "static"):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/api/ping")
def ping():
    return {"ok": True}
