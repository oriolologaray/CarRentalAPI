from pydantic import BaseModel


class Car(BaseModel):
    id: str
    make: str
    model: str
    color: str
