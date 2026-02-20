# FangstLog API
# Skelet til FastAPI applikation — Kiro udfylder dette i Øvelse 3
# Baseret på .kiro/specs/fangst-registrering/

from fastapi import FastAPI

app = FastAPI(
    title="FangstLog API",
    description="Fiktivt fangstregistreringssystem til læringsformål",
    version="0.1.0",
)


@app.get("/")
def rod():
    return {"besked": "Velkommen til FangstLog API. Se /docs for dokumentation."}


# TODO: Implementér POST /fangster
# TODO: Implementér GET /fangster (med dato-filtrering)
# TODO: Implementér GET /fangster/{id}
# TODO: Implementér DELETE /fangster/{id}
