from database import get_db  # Import database connection

@router.post("/predict-price/")
def predict_price(input_data: PricePredictionInput, db=Depends(get_db)):
    features = np.array([[input_data.crop_type, input_data.region, input_data.season, input_data.quantity]])
    predicted_price = model.predict(features)[0]

    # Save to database
    db.execute(
        "INSERT INTO predictions (crop_type, region, season, quantity, predicted_price) VALUES (?, ?, ?, ?, ?)",
        (input_data.crop_type, input_data.region, input_data.season, input_data.quantity, predicted_price)
    )
    db.commit()

    return {"predicted_price": round(float(predicted_price), 2)}
