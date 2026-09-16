from datetime import datetime
from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import Product
from schemas import ProductCreate

def create_product(db: Session, product: ProductCreate):
    current_time = datetime.now()

    new_product = Product(
        name=product.name,
        category=product.category,
        description=product.description,
        product_image=product.product_image,
        sku=product.sku,
        unit_of_measure=product.unit_of_measure,
        lead_time=product.lead_time,
        created_date=current_time,
        updated_date=current_time
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def get_products(db: Session, page: int = 1):
    products_per_page = 10

    skip = (page - 1) * products_per_page

    products = (
        db.query(Product)
        .offset(skip)
        .limit(products_per_page)
        .all()
    )
    return products


def get_product(db: Session, product_id: int):
    product = (
        db.query(Product)
        .filter(Product.product_id == product_id)
        .first()
    )
    return product


def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):
    product = (
        db.query(Product)
        .filter(Product.product_id == product_id)
        .first()
    )

    if product is None:
        return None

    updated_fields = product_data.model_dump(exclude_unset=True)

    for field, value in updated_fields.items():
        setattr(product, field, value)

    product.updated_date = datetime.now()

    db.commit()
    db.refresh(product)

    return product



