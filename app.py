from fastapi import FastAPI
import os

app = FastAPI(title="OrbitGuard API", description="Monitoramento de Telemetria Orbital")

# Critério de Segurança: Lendo do Key Vault (injetado como Env Var)
# Se não achar, usa um fallback seguro local
API_SECRET_KEY = os.getenv("SPACE_API_KEY", "chave-secreta-local-desenvolvimento")

@app.get("/")
def home():
    return {
        "produto": "OrbitGuard API",
        "propósito": "Plataforma de monitoramento de telemetria e integridade de microssatélites em órbita baixa (LEO).",
        "ODS_conectado": "ODS 9 - Indústria, Inovação e Infraestrutura",
        "equipe": "Márcio Hitoshi Tahyra, Aline Fernandes, Camilly Ishida, Julia Galvão, Jéssica Costacurta",
        "status_infraestrutura": "100% Operacional"
    }

@app.get("/telemetria/atual")
def get_telemetry():
    # Rota que simula os dados que o seu pipeline ou IA consumiria
    return {
        "satellite_id": "FLIP-SAT-01",
        "altitude_km": 540.2,
        "battery_level_pct": 94.5,
        "panel_temperature_c": 22.4,
        "radiation_index_gy": 0.012,
        "authenticated_session": API_SECRET_KEY[:5] + "******"
    }