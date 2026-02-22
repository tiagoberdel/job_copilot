from google import genai
from app.core.config import settings
from app.schemas import DatosOferta, Oferta
import json

client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def analizar_texto_con_ia(oferta: Oferta) -> DatosOferta:
    instruccion = f"Extrae los datos de esta oferta laboral: {oferta.oferta}"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=instruccion,
        config={
            'response_mime_type': 'application/json',
            'response_schema': DatosOferta,
        }
    )
    texto_ia = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(texto_ia)
   

def analizar_texto_oferta_mock(texto: str) -> dict:
    return {
        "titulo": "Backend Developer",
        "empresa": "Empresa Demo",
        "salario": "No especificado",
        "cualidades": ["Python", "FastAPI"]
    }