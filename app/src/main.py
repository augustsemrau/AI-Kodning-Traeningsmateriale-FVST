# FangstLog API
# Dette er applikationsskelettet. Kiro udfylder dette i Øvelse 3.

from fastapi import FastAPI

app = FastAPI(
    title="FangstLog API",
    description="Fiktivt fangstregistreringssystem til læringsformål",
    version="0.1.0",
)


@app.get("/")
def rod():
    return {"besked": "Velkommen til FangstLog API. Se /docs for dokumentation."}
