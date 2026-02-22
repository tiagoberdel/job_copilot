from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Oferta(BaseModel):
    oferta: str
class DatosOferta(BaseModel):
    titulo: str
    empresa: str
    ubicacion: str
    descripcion: str
    cualidades: Optional[str] = None
    seniority: Optional[str] = None
    salario: Optional[int] = None
