import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DEDALUS_API_KEY = os.getenv("DEDALUS_API_KEY")
if not DEDALUS_API_KEY:
    raise ValueError("Please set DEDALUS_API_KEY in .env")

# Initialize Dedalus client and runner
client = AsyncDedalus(api_key=DEDALUS_API_KEY)
runner = DedalusRunner(client)

# FastAPI app
app = FastAPI(title="Easel: AI Art Curator")

# Request model
class GalleryRequest(BaseModel):
    theme: str

# Endpoint to generate gallery
@app.post("/curate")
async def curate(req: GalleryRequest):
    theme = req.theme
    response = await runner.run(
        input=f"Generate a mini art exhibition for theme '{theme}'. Return in markdown with 3 artworks.",
        model="openai/gpt-4o-mini"
    )
    return {"gallery": response.final_output}

# Optional: root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Easel: AI Art Curator MCP Server!"}

# Local test runner
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
