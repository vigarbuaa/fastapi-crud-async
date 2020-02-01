from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)

class PersonSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    idcard: str = Field(..., min_length=3, max_length=50)
    hometown: str = Field(..., min_length=3, max_length=50)
    address: str = Field(..., min_length=3, max_length=50)

class NoteDB(NoteSchema):
    id: int

class PersonDB(PersonSchema):
    id: int