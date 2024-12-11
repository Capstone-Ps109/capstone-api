from pydantic import BaseModel

class InputData(BaseModel):
    Nitrogen: int
    Phosphorus: int
    Potassium: int
    Temperature: float
    Humidity: float
    pH_Value: float
    Rainfall: float