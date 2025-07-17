# 03_query_parameters.py

from fastapi import FastAPI, Query, HTTPException, status

app = FastAPI()


@app.get("/search", status_code=status.HTTP_200_OK)
async def search_items(
    keyword: str = Query(
        ...,  # Required parameter
        min_length=3,
        max_length=50,
        description="Search keyword to look for in item names."
    ),
    limit: int = Query(
        10,  # Default value if not provided
        ge=1,
        le=100,
        description="Maximum number of items to return. Default is 10."
    )
):
    """
    Search Items Endpoint:
    - **keyword** (Required): String query parameter (min 3, max 50 chars).
    - **limit** (Optional): Controls number of results (1 to 100, default=10).
    - Returns a simulated list of matching items.
    """

    # Simulate empty result (in real applications, this would query a database)
    if keyword.lower() == "nothing":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No items found matching keyword '{keyword}'."
        )

    # Simulate a fake result list
    results = [f"Item {i+1} related to '{keyword}'" for i in range(limit)]

    return {
        "keyword": keyword,
        "limit": limit,
        "results": results
    }


# To run:
# uvicorn 01_basics.03_query_parameters:app --reload
# Example usage:
# http://127.0.0.1:8000/search?keyword=phone&limit=5