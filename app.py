from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="OrbitGuard API", description="Monitoramento de Telemetria Orbital")

API_SECRET_KEY = os.getenv("SPACE_API_KEY", "chave-secreta-local-desenvolvimento")

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OrbitGuard API | Telemetria Espacial</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
            
            body {
                margin: 0;
                padding: 0;
                background-color: #0b0c10;
                color: #c5c6c7;
                font-family: 'Inter', sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                background-image: radial-gradient(circle at top right, #1f2833, #0b0c10);
            }
            .container {
                max-width: 800px;
                background: rgba(31, 40, 51, 0.8);
                padding: 40px;
                border-radius: 15px;
                border: 1px solid #66fcf1;
                box-shadow: 0 0 20px rgba(102, 252, 241, 0.2);
                text-align: center;
            }
            h1 {
                font-family: 'Orbitron', sans-serif;
                color: #66fcf1;
                font-size: 3em;
                margin-bottom: 10px;
                letter-spacing: 2px;
            }
            .subtitle {
                font-size: 1.2em;
                color: #45a29e;
                margin-bottom: 30px;
            }
            .info-box {
                background: #1f2833;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: left;
                border-left: 4px solid #45a29e;
            }
            .info-box h3 {
                color: #66fcf1;
                margin-top: 0;
            }
            .endpoint {
                display: inline-block;
                background: #0b0c10;
                color: #66fcf1;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                font-family: monospace;
                font-size: 1.1em;
                border: 1px dashed #45a29e;
                transition: 0.3s;
                margin-top: 20px;
            }
            .endpoint:hover {
                background: #45a29e;
                color: #0b0c10;
            }
            .footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>OrbitGuard API</h1>
            <div class="subtitle">Plataforma de Monitoramento de Telemetria Orbital</div>
            
            <div class="info-box">
                <h3>O Problema</h3>
                <p>Microssatélites em órbita baixa (LEO) sofrem com a falta de padronização na recepção de dados de saúde do equipamento. A OrbitGuard atua como um hub centralizado para receber, validar e monitorar métricas vitais como bateria, temperatura e altitude.</p>
            </div>

            <div class="info-box">
                <h3>Conexão ODS</h3>
                <p><strong>ODS 9 - Indústria, Inovação e Infraestrutura:</strong> Fomentamos a democratização do acesso ao espaço fornecendo uma infraestrutura de software resiliente e inovadora para o ecossistema de satélites.</p>
            </div>

            <a href="/telemetria/atual" class="endpoint" target="_blank">Acessar Endpoint de Telemetria (JSON) ➔</a>

            <div class="footer">
                <p><strong>Equipe de Engenharia:</strong> Márcio Hitoshi Tahyra (RM552511) & Jéssica Witzler Costacurta (RM99068)</p>
                <p>Status da Infraestrutura: 100% Operacional na Azure (Secured by Key Vault)</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/telemetria/atual")
def get_telemetry():
    return {
        "satellite_id": "FLIP-SAT-01",
        "altitude_km": 540.2,
        "battery_level_pct": 94.5,
        "panel_temperature_c": 22.4,
        "radiation_index_gy": 0.012,
        "authenticated_session": API_SECRET_KEY[:5] + "******"
    }