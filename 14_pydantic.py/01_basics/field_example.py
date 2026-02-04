from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str,int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length= 3,
        max_length=50,
        description="Employee Name",
        examples="Ritick Bhardwaz"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge = 10000
    )


cart_data = {
    "user_id": 123,
    "items": ["laptop", "Mouse", "keyboard"],
    "quantities": {'laptop': 1, "mouse": 2, "keyboard": 3}
}


cart = Cart(**cart_data)

print (cart)