from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins in CORS settings (not recommended for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],  # Replace with the list of allowed HTTP methods
    allow_headers=["*"],  # Replace with the list of allowed HTTP headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}