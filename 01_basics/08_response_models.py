# 08_response_models.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

# Create FastAPI app instance
app = FastAPI()


# =========================
# Pydantic Models (Schemas)
# =========================

class ItemIn(BaseModel):
    """
    Input Model:
    Used for creating/updating items (client sends this).
    """
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(None, max_length=300)
    price: float = Field(..., gt=0)
    in_stock: bool


class ItemOut(BaseModel):
    """
    Response Model:
    Used to control what data is sent back to the client.
    Excludes sensitive/internal fields.
    """
    name: str
    description: str
    price: float


# Simulated Database (In-memory)
fake_db = []


# =====================
# POST Route (Create Item)
# =====================

@app.post("/items/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemIn):
    """
    POST Endpoint:
    - Accepts ItemIn (request body).
    - Stores the item in the fake database.
    - Returns ItemOut (response model) to filter output.
    """
    fake_db.append(item.dict())
    return item  # Response model automatically filters output


# =====================
# GET Route (List All Items)
# =====================

@app.get("/items/", response_model=List[ItemOut], status_code=status.HTTP_200_OK)
async def get_all_items():
    """
    GET Endpoint:
    - Returns all items using ItemOut response model.
    - Filters out unnecessary/sensitive fields automatically.
    """
    return fake_db


# =====================
# GET Route (Retrieve Item by Index)
# =====================

@app.get("/items/{item_index}", response_model=ItemOut)
async def get_item(item_index: int):
    """
    GET Endpoint with Path Parameter:
    - item_index: Index of the item in the fake database.
    - Returns ItemOut or raises 404 error if index is invalid.
    """
    if item_index < 0 or item_index >= len(fake_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item at index {item_index} not found."
        )

    return fake_db[item_index]


# Run the app using:
# uvicorn 01_basics.07_response_models:app --reload