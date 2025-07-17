# 02_path_parameters.py

from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a GET route with a path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Path Parameter Example:
    - URL: /items/{item_id}
    - Accepts item_id as an integer directly from the URL.
    - Example: /items/42 will return {"item_id": 42}
    """
    return {"item_id": item_id}

# To run this file:
# uvicorn 01_basics.02_path_parameters:app --reload