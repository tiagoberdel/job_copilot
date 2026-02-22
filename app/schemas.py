from pydantic import BaseModel, Field
from typing import Optional, List

class Oferta(BaseModel):
    oferta: str

class DatosOferta(BaseModel):
    titulo: str = Field(description="El nombre del puesto de trabajo")
    empresa: str = Field(description="Nombre de la compañía que contrata")
    ubicacion: str = Field(description="Ciudad o si es Remoto/Híbrido")
    descripcion: str = Field(description="Resumen breve de la posición")
    cualidades: List[str] = Field(default_factory=list, description="Lista de tecnologías o habilidades requeridas")
    seniority: Optional[str] = Field(None, description="Junior, Mid, Senior, etc.")
    salario: Optional[str] = None