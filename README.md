[README.md](https://github.com/user-attachments/files/27102823/README.md)
# 🤖 WhatsApp Bot — CreateC3D

Automated WhatsApp customer service bot built for **CreateC3D**, a 3D printing and digital manufacturing business based in Colombia. Built with Python and FastAPI, integrated with the Twilio API, and deployed to the cloud.

---

## 🧠 Why I built this

CreateC3D is a business I founded and have been building for 4 years. As demand grew, I was spending hours every day answering the same customer questions — services, pricing, appointments, payment methods.

I didn't want to hire someone just to answer WhatsApp messages. So I learned to program and built the solution myself.

This bot handles the first layer of customer interaction automatically, 24/7, so I can focus on the actual work: design, production, and client results.

---

## ⚙️ How it works

1. A customer sends a WhatsApp message to the business number
2. Twilio receives the message and forwards it to this app via webhook
3. FastAPI processes the message and generates the appropriate response
4. The response is sent back to the customer via Twilio — instantly, automatically

### Menu options handled by the bot

| Input | Response |
|-------|----------|
| `hola`, `menu`, `hi`, `start` | Welcome message + full menu |
| `1` / `servicio` | List of services |
| `2` / `precio` | Pricing |
| `3` / `cita` | Appointment booking link (Calendly) |
| `4` / `pago` | Payment methods accepted |
| `5` / `asesor` | Transfer to human agent |

---

## 🛠️ Tech stack

- **Python 3.10+**
- **FastAPI** — async web framework for the webhook endpoint
- **Twilio API** — WhatsApp Business messaging
- **httpx** — async HTTP client
- **python-dotenv** — environment variable management
- **Heroku / Procfile** — cloud deployment

---

## 🚀 Setup & local development

### 1. Clone the repo

```bash
git clone https://github.com/mono0119/bot-whatsapp.git
cd bot-whatsapp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

### 4. Run locally

```bash
uvicorn main:app --reload
```

### 5. Expose locally with ngrok (for Twilio webhook testing)

```bash
ngrok http 8000
```

Then paste the ngrok URL into your Twilio sandbox webhook settings:
`https://your-ngrok-url.ngrok.io/webhook`

---

## ☁️ Deployment

This app is configured for Heroku deployment via `Procfile`:

```
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000}
```

---

## 📁 Project structure

```
bot-whatsapp/
├── main.py            # FastAPI app — webhook logic and bot responses
├── requirements.txt   # Python dependencies
├── Procfile           # Heroku deployment config
└── .env               # Environment variables (not committed)
```

---

## 🏭 About CreateC3D

CreateC3D is a Colombian business specializing in 3D printing, digital manufacturing, and design services. Founded in 2021, it has grown from a single printer to a full-service operation offering consulting, production, coaching, and training for individuals and businesses.

This bot is one of several internal tools built to automate operations and scale without proportionally growing overhead.

---

## 👤 Author

**John Harvey Alvarez Sarria**
Founder, CreateC3D | Bilingual Developer | English Teacher
📍 Zarzal, Valle del Cauca, Colombia
🌐 Open to remote opportunities

---

## 📄 License

MIT License — free to use and adapt with attribution.
