from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from model import Product
from database_connection import PostgresConnection
from sqlalchemy import text

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pgObj=PostgresConnection()

@app.get("/products")
def get_products():
    with pgObj.engine.connect() as conn:
        result=conn.execute(text("SELECT * FROM products"))
        return [dict(row._mapping) for row in result]

@app.get("/products/{id}")
def get_product(product_id:int):
    with pgObj.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM products p where p.id = :id"),{"id":product_id}).fetchone()

        if result is None:
            return "Product not found with id",product_id
        return [dict(result._mapping)]

@app.post("/products")
def add_product(product:Product):
    with pgObj.engine.begin() as conn:
        result=conn.execute(text("""Insert into products(name, price, description, quantity) 
                     Values (:name, :price, :description, :quantity) 
                     Returning id"""),
                     {
                         "name":product.name,
                         "price":product.price,
                         "description":product.description,
                         "quantity":product.quantity
                     }
                     )
        product_id=result.scalar()
    return "Product added with id",product_id

@app.put("/products/{id}")
def update_product(id:int,product_to_update:Product):
    with pgObj.engine.begin() as conn:
        result=conn.execute(text("""
        UPDATE products 
        SET name = :name, price = :price, description = :description, quantity = :quantity
        WHERE id = :id
        """),
            {
                "name":product_to_update.name,
                "price":product_to_update.price,
                "description":product_to_update.description,
                "quantity":product_to_update.quantity,
                "id":id
            }
                            )
        if result.rowcount == 0:
            return "Product not found with id",id
        else:
            return "Product updated with id",id

@app.delete("/products/{id}")
def delete_product(id:int):
    with pgObj.engine.begin() as conn:
        result=conn.execute(text("DELETE FROM products where id = :id"),{"id":id})

        if result.rowcount == 0:
            return "Product not found with id",id
        else:
            return "Product deleted with id",id