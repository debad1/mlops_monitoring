import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app

# Initialiser le modèle
heart_attack_model = joblib.load("./heart_attack_prediction_model.joblib")

# Définition des compteurs Prometheus
survived_counter = Counter("survived", "Counter for survived predictions")
not_survived_counter = Counter(
    "not_survived", "Counter for not survived predictions")

app = FastAPI()

# Monter l'application de métriques Prometheus
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/heart_attack")
def prediction_api(time: int, ejection_fraction: float, serum_creatinine: float):
    # Préparer les données pour la prédiction
    x = pd.DataFrame([[time, ejection_fraction, serum_creatinine]], columns=[
                     'time', 'ejection_fraction', 'serum_creatinine'])

    # Faire la prédiction
    prediction = heart_attack_model.predict(x)
    survived = int(prediction[0]) == 1

    # Incrémenter le compteur approprié
    if survived:
        survived_counter.inc()
    else:
        not_survived_counter.inc()

    return {"survived": survived}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
