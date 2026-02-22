from fastapi import APIRouter, HTTPException
from ..schemas import Oferta, DatosOferta
from app.services.job_analyzer import analizar_texto_con_ia

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])

@router.post("/analizar", response_model=DatosOferta)
async def analizar_oferta(oferta: Oferta):
    """
    Recibe texto crudo de una oferta laboral,
    lo procesa con la IA de Gemini,
    y devuelve los datos estructurados.
    """
    try:
        resultado = await analizar_texto_con_ia(oferta) 
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el análisis: {str(e)}")