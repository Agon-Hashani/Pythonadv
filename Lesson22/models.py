from pydantic import BaseModel, ValidationInfo, field_validatior, constr, conint

class User(BaseModel):
    id: int
    name: str
    age: int

    @field_serializer('age')
    def age_must_be_positive(cls, v, info: FieldSerializationInfo):
        if v <= 0:
            raise  ValueError("Age must be positive")
        return v

try:
    user = User(id=1, name='John Doe', age=-1)
except ValueError as e:
    print(e)

class Address(BaseModel):
    street: str
    city: str

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)