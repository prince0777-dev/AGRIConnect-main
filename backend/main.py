from fastapi import FastAPI
from routes import price_prediction

app = FastAPI(title="AgriConnect Backend")

# Include prediction route
app.include_router(price_prediction.router)

@app.get("/")
def home():
    return {"message": "Welcome to AgriConnect API"}
