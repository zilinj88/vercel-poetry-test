from fastapi import FastAPI
from common.constants import MESSAGE

app = FastAPI(
    title="Aerial Data API",
    version="0.1.0",
    description="Aerial Data API",
)

@app.get('/')
def api():
  return MESSAGE