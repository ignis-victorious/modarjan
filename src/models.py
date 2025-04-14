


#  ________________
#  Import LIBRARIES
from sqlmodel import SQLModel, Field
#  Import FILES
#  ________________





# Hero model
class Hero(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    secret_name: str
    age: int | None 
