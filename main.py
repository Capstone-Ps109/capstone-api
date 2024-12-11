from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn

from models.input_schema import InputData
from models.crop_model import RotasiTanaman
from services.auth_service import validate_token
from services.firestore_service import FirestoreLogger
from services.model_service import download_model
from config import MODEL_PATH, STORAGE_BUCKET, STORAGE_MODEL_PATH

# Download model before starting
download_model(STORAGE_BUCKET, STORAGE_MODEL_PATH, MODEL_PATH)

# Inisialisasi engine prediksi
engine = RotasiTanaman(MODEL_PATH)
firestore_logger = FirestoreLogger()

# FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API untuk Rekomendasi Rotasi Tanaman"}

@app.post("/predict")
async def predict_manual(
    data: InputData, 
    token: str = Query(..., description="Authentication token")
):
    try:
        # Debug: Print token yang diterima
        print(f"Received Token: {token}")

        # Validasi token
        user_id = validate_token(token)
        print(f"Validated User ID: {user_id}")

        # Sisa kode prediksi
        input_data = data.dict()
        preprocessed_data = engine.preprocessing(input_data)
        predictions = engine.predict(preprocessed_data)
        top_crops = engine.get_top_crops(predictions)
        
        soil_quality = engine.classify_soil_quality(
            input_data["Humidity"], 
            input_data["pH_Value"]
        )

        prediction_result = {
            "input": input_data,
            "predictions": top_crops,
            "soil_quality": soil_quality
        }

        # Log ke Firestore
        firestore_logger.log_prediction(user_id, prediction_result)

        return prediction_result
    except Exception as e:
        print(f"Prediction Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/prediction-history")
async def get_prediction_history(
    token: str = Query(..., description="Authentication token")
):
    try:
        # Validasi token dan dapatkan user_id
        user_id = validate_token(token)

        # Ambil history prediksi
        prediction_history = firestore_logger.get_prediction_history(user_id)

        return {
            "user_id": user_id,
            "total_predictions": len(prediction_history),
            "history": prediction_history
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Jalankan server FastAPI
if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000
    )