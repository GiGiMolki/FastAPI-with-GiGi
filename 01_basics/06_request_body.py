# 06_request_body.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict

# Initialize FastAPI app
app = FastAPI()


# Define Pydantic model for request body
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item.")
    description: str = Field(None, max_length=300, description="Optional detailed description.")
    price: float = Field(..., gt=0, description="Price of the item. Must be greater than 0.")
    in_stock: bool = Field(..., description="Availability of the item: True or False.")


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """
    Create Item Endpoint:
    - Accepts structured JSON data as request body.
    - Validates fields using the Item Pydantic model.
    - Returns the created item details as confirmation.
    """

    # Example server-side validation (simulate duplicate check)
    if item.name.lower() == "test item":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item with this name already exists."
        )

    # Simulate item creation and return the item
    return {
        "message": "Item created successfully.",
        "item": item
    }


# To run:
# uvicorn 01_basics.06_request_body:app --reload

# Example request body (JSON):
# {
#     "name": "Wireless Mouse",
#     "description": "A high-precision wireless mouse.",
#     "price": 29.99,
#     "in_stock": true
# }

# Example response  body (JSON):
# {
#   "message": "Item created successfully.",
#   "item": {
#       "name": "Wireless Mouse",
#       "description": "A high-precision wireless mouse.",
#       "price": 29.99,
#       "in_stock": true
#   }


# Simulated database (in-memory dictionary)
fake_db: Dict[int, dict] = {
    1: {"name": "Laptop", "description": "High-end gaming laptop.", "price": 1500.00, "in_stock": True},
    2: {"name": "Smartphone", "description": "Latest model smartphone.", "price": 999.99, "in_stock": True},
}


# Pydantic model for item input
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(None, max_length=300)
    price: float = Field(..., gt=0)
    in_stock: bool


@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
async def update_item(item_id: int, item: Item):
    """
    PUT Endpoint to Update Item:
    - item_id: Path parameter to identify item.
    - item: Request body containing updated item data.
    - Returns updated item or 404 if item_id not found.
    """

    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found."
        )

    fake_db[item_id] = item.dict()

    return {
        "message": f"Item ID {item_id} updated successfully.",
        "item": fake_db[item_id]
    }
    
# 📬 Sample Request:
# PUT /items/1

# {
#   "name": "Gaming Laptop",
#   "description": "Updated description for gaming laptop.",
#   "price": 2000.00,
#   "in_stock": true
# }

# 📥 Sample Response (200 OK):
# {
#   "message": "Item ID 1 updated successfully.",
#   "item": {
#       "name": "Gaming Laptop",
#       "description": "Updated description for gaming laptop.",
#       "price": 2000.0,
#       "in_stock": true
#   }


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """
    DELETE Endpoint to Remove Item:
    - item_id: Path parameter to identify item.
    - Returns 204 No Content on successful deletion or 404 if item not found.
    """

    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found."
        )

    del fake_db[item_id]

    # 204 No Content: return nothing
    return

# 📬 Sample Request:
# DELETE /items/2
# (No body required.)

# 📥 Sample Response (204 No Content):
# Response body is empty.

# ❌ Error Example:
# DELETE /items/99
# Response (404 Not Found):
# {
#   "detail": "Item with ID 99 not found."
# }

# To run:
# uvicorn 01_basics.06_request_bod:app --reload