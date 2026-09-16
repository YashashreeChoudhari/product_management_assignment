from sqlalchemy import BigInteger, Column, DateTime, Enum, Integer, String, Text
from database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = Column(String(100), nullable=False)

    category = Column(
        Enum("finished", "semi-finished", "raw"),
        nullable=False
    )

    description = Column(String(250), nullable=True)

    product_image = Column(Text, nullable=True)

    sku = Column(String(100), nullable=False)

    unit_of_measure = Column(
        Enum(
            "mtr",
            "mm",
            "ltr",
            "ml",
            "cm",
            "mg",
            "gm",
            "unit",
            "pack"
        ),
        nullable=False
    )

    lead_time = Column(Integer, nullable=False)

    created_date = Column(DateTime, nullable=False)

    updated_date = Column(DateTime, nullable=False)