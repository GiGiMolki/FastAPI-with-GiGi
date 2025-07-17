# 📊 HTTP Status Codes in FastAPI

FastAPI uses standard **HTTP Status Codes** to indicate the result of API operations. Below is a reference table of commonly used status codes:

| Status Code | Name                  | Description                                                       |
|-------------|-----------------------|-------------------------------------------------------------------|
| **200 OK**  | Success               | Request succeeded. Response contains the requested data.          |
| **201 Created** | Resource Created  | Request succeeded and a new resource has been created.            |
| **204 No Content** | No Content     | Request succeeded but there is no content to return.              |
| **400 Bad Request** | Bad Request   | The request was invalid (e.g., validation errors, incorrect data).|
| **401 Unauthorized** | Unauthorized | Authentication required or failed.                                |
| **403 Forbidden** | Forbidden       | Authenticated but access is forbidden.                            |
| **404 Not Found** | Not Found       | Requested resource could not be found.                            |
| **409 Conflict** | Conflict         | Request could not be processed due to a conflict (e.g., duplicate entry). |
| **422 Unprocessable Entity** | Validation Error | Input validation failed (common in FastAPI for request body errors). |
| **500 Internal Server Error** | Server Error | Generic server error. Unexpected condition occurred.              |

---

## ✅ Examples in FastAPI:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/example", status_code=status.HTTP_200_OK)
async def example_endpoint():
    return {"message": "Success!"}

@app.get("/not_found")
async def not_found_endpoint():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Resource not found."
    )
```


```python
# 02_path_parameters.py

from fastapi import FastAPI, Path, HTTPException, status

app = FastAPI()


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(
    item_id: int = Path(
        ...,
        title="Item ID",
        description="The unique identifier for the item. Must be a positive integer.",
        gt=0,  # item_id must be greater than 0
        example=42
    )
):
    """
    Retrieve an item by its unique item_id.

    - **item_id**: Positive integer path parameter.
    - Returns item details if found.
    - Raises 404 error if item_id exceeds simulated database limit.
    """

    # Simulated validation: Item IDs above 1000 are treated as non-existent
    if item_id > 1000:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found."
        )

    # Return the valid item_id
    return {
        "item_id": item_id,
        "description": f"Details about item {item_id}."
    }


# How to run this file:
# uvicorn 01_basics.02_path_parameters:app --reload
```