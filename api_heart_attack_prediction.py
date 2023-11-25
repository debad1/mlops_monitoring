import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app
from starlette.responses import JSONResponse

# survived_counter = Counter("survived", "Counter for survived")
# not_survived_counter = Counter("not_survived", "Counter for not survived")

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/heart_attack")
def prediction_api(time: int, ejection_fraction: float, serum_creatinine: float):
    heart_attack_model = joblib.load("./titanic_model.joblib")
    x = [time, ejection_fraction, serum_creatinine]
    prediction = heart_attack_model.predict(pd.DataFrame(x).transpose())

    #    if survived:
    #        survived_counter.inc()
    #    else:
    #       not_survived_counter.inc()
    return prediction


@app.get("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
