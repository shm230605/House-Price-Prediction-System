from pydantic import BaseModel

class HouseInput(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    location_score: int
    age: int