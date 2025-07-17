# 📦 Handling Request Body in FastAPI

In APIs, clients often send structured data to the server. FastAPI simplifies handling such data using **Pydantic models**, which enable automatic **data parsing, validation, and documentation**.

---

## 📑 What is a Request Body?

- **Request Body** is the part of an HTTP request where clients send data (usually in JSON format) when creating or updating resources.
- Example: When a user submits a form, the data (name, email, etc.) is sent in the request body.

In FastAPI, request body data is received as **Python classes** defined using **Pydantic**.

---

## 🛠️ Pydantic Models

- Pydantic is a powerful data validation library.
- FastAPI uses Pydantic models to:
  - Parse incoming JSON data automatically.
  - Validate data types, lengths, ranges, and other constraints.
  - Auto-generate OpenAPI docs with field descriptions.

Example Model:

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str = Field(None, max_length=200)
    price: float = Field(..., gt=0)
    in_stock: bool = Field(default=True)
  ```

### 📥 Receiving Request Body in FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

FastAPI automatically:
- Parses incoming JSON.
- Converts it to an Item object.
- Performs validation.
- Returns clear error messages for invalid data.	•	

### 📊 Status Codes with Request Body

| Status Code | Purpose                                |
|-------------|----------------------------------------|
| 201 Created | Resource created successfully          |
| 400 Bad Request | Input data is invalid              |
| 422 Unprocessable Entity | Validation failed (handled automatically by FastAPI) |

```python
# Use the status module for better readability:
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
```

### ⚠️ Handling Invalid Data
- FastAPI automatically returns 422 Unprocessable Entity if the input fails validation.
- You can also raise manual exceptions using HTTPException for custom business rules:

```python
from fastapi import HTTPException, status

if item.price > 10000:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Price exceeds allowed maximum."
    )
```

### 📊 Benefits of Using Pydantic Models

| Benefit            | Explanation                                        |
|--------------------|----------------------------------------------------|
| Data Validation    | Ensures incoming data meets required formats.      |
| Automatic Docs     | Fields appear in `/docs` with descriptions.        |
| Clear Error Handling | Invalid data triggers structured error responses. |
| Easy Maintenance   | Models are Python classes — easy to read & reuse.  |

### 📚 Example API Call

- Endpoint: POST /items

Body Example:
```json
{
  "name": "Wireless Mouse",
  "description": "Ergonomic wireless mouse.",
  "price": 25.99,
  "in_stock": true
}
```

### 📌 Summary
- Use Pydantic models to handle and validate request bodies.
- Use status codes to indicate operation results.
- Use HTTPException for custom error messages.
- FastAPI automates much of the request body parsing and validation process.

# 📘 Understanding `app`, `POST`, `PUT`, and `DELETE` in FastAPI

## ✅ `app = FastAPI()`

- Creates an instance of the FastAPI application.
- This object (`app`) is responsible for handling all incoming HTTP requests and routing them to appropriate functions.
- You define API endpoints using decorators like `@app.get()`, `@app.post()`, etc.

---

## 📤 `@app.post()` – Creating Resources

- **POST** method is used to **create new resources**.
- Expects data (usually JSON) in the **request body**.
- Commonly used for:
  - Creating new users, products, records, etc.
- FastAPI handles automatic **data validation** using **Pydantic models**.
- Returns **201 Created** status code when resource is successfully created.

**Example:**

```python
@app.post("/items/", status_code=201)
async def create_item(item: Item):
    return {"message": "Item created", "item": item}
```

## ♻️ @app.put() – Updating Resources
- PUT method is used to update existing resources completely.
- Requires both:
- Path Parameter to identify which resource to update.
- Request Body containing updated resource data.
- PUT replaces the entire resource with the new data.
- Returns 200 OK status code upon successful update.

**Example:**
```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    fake_db[item_id] = item.dict()
    return {"message": "Item updated", "item": fake_db[item_id]}
```
## 🗑️ `@app.delete()` – Deleting Resources

- **DELETE** method is used to **remove existing resources**.
- Requires a **Path Parameter** to identify which resource to delete.
- Returns **204 No Content** status code after successful deletion, indicating that the operation was successful but there is **no response body**.

### ✅ Example:

```python
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    del fake_db[item_id]
    return
```

### 📊 Summary Table

| HTTP Method | Purpose           | Input                          | Typical Status Code |
|-------------|-------------------|--------------------------------|----------------------|
| POST        | Create Resource   | Request Body (JSON)            | 201 Created          |
| PUT         | Update Resource   | Path Parameter + Request Body  | 200 OK               |
| DELETE      | Delete Resource   | Path Parameter                 | 204 No Content       |


## 🚀 How FastAPI Works

- FastAPI reads the HTTP request.
- Automatically parses and validates incoming data using **Pydantic models**.
- Routes the request to the appropriate function based on method (`POST`, `PUT`, `DELETE`).
- Generates appropriate HTTP responses, including status codes and JSON output.
- Enables automatic API documentation using **Swagger UI** at `/docs`.