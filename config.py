import os

# Model Configuration
MODEL_PATH = os.getenv('MODEL_PATH', 'downloads/optimized_model.tflite')  # Ubah path ke lokasi download
STORAGE_BUCKET = os.getenv('STORAGE_BUCKET', 'model-api109')
STORAGE_MODEL_PATH = os.getenv('STORAGE_MODEL_PATH', 'model-prod/optimized_model.tflite')  # Path di cloud storage

# Auth API Configuration
AUTH_API_ENDPOINT = os.getenv(
    'AUTH_API_ENDPOINT', 
    'https://auth-api-1082812442001.asia-southeast2.run.app/auth'
)

# Crop Labels
CROP_LABELS = {
    0: "Blackgram",
    1: "KidneyBeans",
    2: "Maize",
    3: "MothBeans",
    4: "MungBean",
    5: "PigeonPeas",
    6: "Rice"
}