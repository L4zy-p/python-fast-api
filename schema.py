from pydantic import BaseModel

# STEP 3 PYDANTIC MODEL
# base class
class ItemBase(BaseModel):
    title: str
    description: str
    price: float

# inherit for on top - request
class ItemCreated(ItemBase):
    pass

# inherit for on top - response
class ItemResponse(ItemBase):
    id: int # return id
    class Config:
        from_attributes = True