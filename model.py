from sqlalchemy import Column, Integer, String
from database import Base

# STEP 2 ORM CLASS
# create orm class
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)

