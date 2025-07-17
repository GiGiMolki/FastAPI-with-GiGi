# 🚀 Introduction to FastAPI and CRUD Operations

## 📌 What is FastAPI?

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on:
- **Standard Python type hints**
- **Pydantic** for data validation
- **Starlette** for web handling (under the hood)

### ⚡ Key Features:
- **Blazing Fast:** Performance similar to Node.js and Go.
- **Easy to Learn:** Minimal boilerplate code with automatic API documentation.
- **Automatic Docs:** Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Data Validation:** Powered by Pydantic.
- **Asynchronous Support:** Handles async/await natively for non-blocking code.

---

## 🛠️ Why Use FastAPI?

| Feature                 | Benefit                                  |
|-------------------------|------------------------------------------|
| Python Type Hints       | Better editor support and code clarity.  |
| Auto Docs               | Interactive Swagger UI out of the box.   |
| High Performance        | Uses Starlette and Pydantic internally.  |
| Easy Validation         | Built-in request and response validation.|
| Async I/O               | Handle high-concurrency applications.    |

---

## 📊 CRUD Operations

In any API, most operations are based on CRUD — a standard database concept.

| CRUD Operation | HTTP Method | Purpose               |
|----------------|------------|------------------------|
| **Create**     | POST       | Add new resources      |
| **Read**       | GET        | Retrieve resources     |
| **Update**     | PUT / PATCH| Modify existing data   |
| **Delete**     | DELETE     | Remove data            |

### 📌 CRUD Example in Real Life:
- **Create**: Registering a new user.
- **Read**: Fetching product listings.
- **Update**: Changing a user's password.
- **Delete**: Removing a blog post.

---

## 💻 CRUD Endpoints Example with FastAPI
Don't worry , you will understand the below code in the later notebooks.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for input data
class Item(BaseModel):
    name: str
    price: float

# Simulate in-memory storage
items_db = []

# CREATE
@app.post("/items")
async def create_item(item: Item):
    items_db.append(item)
    return {"message": "Item added successfully", "item": item}

# READ
@app.get("/items")
async def read_items():
    return {"items": items_db}

# UPDATE
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"message": "Item updated", "item": item}

# DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}