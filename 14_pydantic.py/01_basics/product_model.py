from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_one = Product(id = 1, name = 'Laptop', price = 999.99, in_stock=True)

product_two = Product(id=2, name="Mouse", price=555)

# p1 = Product(**product_one)

# p2 = Product(**product_two)

# print(p1)
# print(p2)