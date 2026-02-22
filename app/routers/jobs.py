from fastapi import APIRouter
from ..schemas import Oferta, DatosOferta
from ..services.job_analyzer import analizar_texto_oferta

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])

@router.post("/analizar", response_model=DatosOferta)
def analizar_oferta(oferta: Oferta):
    """
    Recibe texto crudo de una oferta laboral,
    lo procesa (IA después),
    y devuelve los datos estructurados.
    """

    resultado = analizar_texto_oferta(oferta.oferta)

    return resultado