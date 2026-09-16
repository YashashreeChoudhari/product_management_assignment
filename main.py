from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import ProductCreate, ProductResponse, ProductUpdate

app = FastAPI()

@app.get("/product/list", response_model=list[ProductResponse])
def list_products(
    page: int = 1,
    db: Session = Depends(get_db)
):
    if page < 1:
        raise HTTPException(
            status_code=400,
            detail="Page number must be greater than 0"
        )

    return crud.get_products(db, page)


@app.get("/product/{pid}/info", response_model=ProductResponse)
def get_product_info(
    pid: int,
    db: Session = Depends(get_db)
):
    product = crud.get_product(db, pid)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@app.post("/product/add", response_model=ProductResponse)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)


@app.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(
    pid: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(db, pid, product)

    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product