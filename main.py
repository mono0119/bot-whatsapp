import os
import re
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
import httpx

load_dotenv()
app = FastAPI()

def get_response(text: str) -> str:
    text = text.strip().lower()
    if re.search(r'\b(hola|menu|start|hi|inicio)\b', text):
        return (
            "Hola! Bienvenido a CreateC3D\n\n"
            "En que te puedo ayudar?\n\n"
            "1 - Ver servicios\n"
            "2 - Ver precios\n"
            "3 - Agendar cita\n"
            "4 - Metodos de pago\n"
            "5 - Hablar con asesor\n"
            "6 - Sobre nosotros\n"
            "7 - Horarios\n"
            "8 - Ubicacion"
        )
    elif re.search(r'\b(1|servicio|servicios)\b', text):
        return "Servicios:\n- Consultoria\n- Auditoria\n- Coaching\n- Capacitacion"
    elif re.search(r'\b(2|precio|precios)\b', text):
        return "Precios:\n- Consultoria: $150\n- Auditoria: $300\n- Coaching: $200"
    elif re.search(r'\b(3|cita|citas)\b', text):
        return "Agenda tu cita aqui:\nhttps://calendly.com/createc3d"
    elif re.search(r'\b(4|pago|pagos)\b', text):
        return "Aceptamos:\n- Tarjeta\n- Transferencia\n- PayPal\n- Zelle"
    elif re.search(r'\b(5|asesor|asesores)\b', text):
        return "Te conectamos con un asesor:\n+57 300 123 4567"
    elif re.search(r'\b(6|nosotros|empresa)\b', text):
        return "Sobre nosotros:\nSomos CreateC3D, una empresa líder en consultoría y capacitación."
    elif re.search(r'\b(7|horario|horarios)\b', text):
        return "Horarios de atención:\nLunes a Viernes de 9:00 am a 6:00 pm"
    elif re.search(r'\b(8|ubicacion|donde)\b', text):
        return "Ubicación:\nNos encontramos en Calle Falsa 123, Ciudad."
    else:
        return "No entendi. Escribe menu para ver las opciones."

@app.post("/webhook")
async def webhook(request: Request):
    try:
        form = await request.form()
        body = str(form.get("Body", ""))
        phone = str(form.get("From", ""))
        print(f"Mensaje de {phone}: {body}")
        response_text = get_response(body)
        sid = os.getenv("TWILIO_ACCOUNT_SID")
        token = os.getenv("TWILIO_AUTH_TOKEN")
        from_num = os.getenv("TWILIO_WHATSAPP_NUMBER")
        url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
        async with httpx.AsyncClient() as client:
            r = await client.post(url,
                data={"From": from_num, "To": phone, "Body": response_text},
                auth=(sid, token))
            print(f"Twilio respondio: {r.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")
    return PlainTextResponse("OK")

@app.get("/")
async def health():
    return {"status": "ok"}
