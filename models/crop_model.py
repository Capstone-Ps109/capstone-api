import numpy as np
import tensorflow as tf
from config import CROP_LABELS

class RotasiTanaman:
    def __init__(self, model_path):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    def categorize_rainfall(self, rainfall_input):
        
        rainfall_mapping = {
            'Rendah': 100.0,    
            'Sedang': 300.0,   
            'Tinggi': 500.0    
        }
        
        return rainfall_mapping.get(rainfall_input, 0.0)
    
    def preprocessing(self, data):
        
        # Konversi kategori curah hujan menjadi nilai numerik
        rainfall_numeric = self.categorize_rainfall(data["Rainfall"])
        
        processed_data = np.array([[
            data["Nitrogen"] / 100.0,
            data["Phosphorus"] / 100.0,
            data["Potassium"] / 100.0,
            (data["Temperature"] - 15) / 10,
            data["Humidity"] / 100.0,
            data["pH_Value"] / 8.0,
            rainfall_numeric / 1000.0
        ]], dtype=np.float32)
        
        return processed_data
    
    def predict(self, preprocessed_data):
        
        self.interpreter.set_tensor(self.input_details[0]['index'], preprocessed_data)
        self.interpreter.invoke()
        predictions = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        return predictions
    
    def get_top_crops(self, predictions):
        
        top_3_indices = predictions.argsort()[-3:][::-1]
        top_3_rotasi_1 = [
            {"crop": CROP_LABELS[idx], "confidence": float(predictions[idx])}
            for idx in top_3_indices[:3]
        ]
        return {"rotasi_1": top_3_rotasi_1}
    
    def classify_soil_quality(self, humidity, pH_value):
    
        if humidity > 80 and pH_value >= 6.5:
            return "Subur"
        elif humidity <= 80 and humidity >= 50:
            return "Lembap"
        else:
            return "Kering"