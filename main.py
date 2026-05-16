# main.py - Bot WhatsApp CREATEC 3D con IA (Gemini)
from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Contexto de CREATEC 3D para la IA
CREATEC_CONTEXT = """
Eres el asistente virtual oficial de CREATEC 3D, una agencia colombiana dirigida por John Alvarez.

SERVICIOS:
1. MARKETING Y BRANDING: Identidad visual completa, campañas digitales medibles, contenido para redes sociales, estrategia de crecimiento.
2. DESARROLLO WEB: Páginas web a medida, tiendas online (e-commerce), landing pages de alta conversión, optimización para Google (SEO).
3. IMPRESIÓN 3D: Prototipos rápidos, piezas funcionales, diseño 3D a medida, modelos personalizados.
4. SOLUCIONES CON IA: Asistentes IA para WhatsApp, automatización de tareas, análisis de datos con IA, integración con sistemas existentes.
5. ASESORÍA VISA USA: Llenado del DS-160, preparación para entrevista consular, simulacros, acompañamiento personal para visa B1/B2.
6. EDUCACIÓN E INGLÉS: Clases de inglés conversacional, preparación de exámenes, formación en IA aplicada, cursos personalizados.

PROCESO:
- Paso 1: Asesoría inicial gratis, sin compromiso
- Paso 2: Propuesta clara con tiempos, alcance y precio honesto
- Paso 3: Ejecución con avances aprobados por el cliente
- Paso 4: Soporte 30 días post-entrega

REGLAS:
- Siempre responde en español
- Sé profesional pero cercano
- Si no sabes algo, ofrece agendar asesoría gratis con John
- Nunca inventes precios específicos, di "depende del alcance" y ofrece cotización
- Respuestas cortas (maximo 2-3 frases) para WhatsApp
"""

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    form_data = await request.form()
    incoming_msg = form_data.get("Body", "").strip().lower()
    
    # Crear respuesta Twilio
    resp = MessagingResponse()
    msg = resp.message()
    
    # Comandos especiales (menu rapido)
    if incoming_msg in ["hola", "menu", "hi", "start"]:
        msg.body("Hola! Soy el asistente de CREATEC 3D. En que puedo ayudarte? Preguntame sobre nuestros servicios, impresion 3D, desarrollo web, visas USA, marketing digital, clases de ingles, o escribe tu pregunta directamente.")
        return Response(content=str(resp), media_type="application/xml")

    if incoming_msg in ["5", "asesor", "humano", "agente"]:
        msg.body("Te transfiero con John o un asesor. Por favor espera un momento...")
        return Response(content=str(resp), media_type="application/xml")
    
    # Respuesta con IA (Gemini)
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(history=[])
        
        prompt = f"{CREATEC_CONTEXT}\n\nCLIENTE: {incoming_msg}\nASISTENTE:"
        response = chat.send_message(prompt)
        
        respuesta_ia = response.text
        msg.body(respuesta_ia)

    except Exception as e:
        msg.body("Lo siento, tuve un problema. Escribe 'asesor' para hablar con un humano o intenta de nuevo.")
        print(f"Error Gemini: {e}")

    return Response(content=str(resp), media_type="application/xml")

@app.get("/")
def health_check():
    return {"status": "CREATEC 3D Bot activo", "version": "2.0-IA"}
