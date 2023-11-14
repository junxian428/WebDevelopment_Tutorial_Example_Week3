from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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


# In-memory database as a placeholder
fake_db = []

# Model for the data
class Item(BaseModel):
    name: str
    description: str = None

# Create operation
@app.post("/items/")
async def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item created successfully", "item": item}

# Read operation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item retrieved successfully", "item": fake_db[item_id]}

# Update operation
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")

    # Update the item in the fake database
    fake_db[item_id] = item
    return {"message": "Item updated successfully", "item": item}

# Delete operation
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")

    # Delete the item from the fake database
    deleted_item = fake_db.pop(item_id)
    return {"message": "Item deleted successfully", "item": deleted_item}

# List all items
@app.get("/items/")
async def list_items():
    return {"message": "Items listed successfully", "items": fake_db}
