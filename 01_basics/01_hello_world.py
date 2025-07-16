# 01_hello_world.py

# Import the FastAPI class
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a route using the decorator
@app.get("/")
async def read_root():
    """
    Root endpoint returning a simple welcome message.
    Accessible at: http://127.0.0.1:8000/
    """
    return {"message": "Hello, GiGi! Welcome to FastAPI."}

# To run this file:
# uvicorn 01_basics.01_hello_world:app --reload
# The --reload flag enables auto-reload on code changes