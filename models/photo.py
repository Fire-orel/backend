from dataclasses import dataclass
from models import BaseModel

@dataclass
class PhotoMas(BaseModel):
    data_aos: str
    img: str