
# Capstone - PlantRO

An application to determine the crop rotation suitable for planting based on soil Ph, rainfall, and soil content.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Capstone-Ps109/capstone-api.git
```

Go to the project directory

```bash
  cd model-api
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

## Endpoint
https://model-api-1082812442001.asia-southeast2.run.app/

## API Reference

#### Predict
- URL : 
  - `/predict?token=`
- Method : 
  - `POST`
- Request Body :
  - `Nitrogen` as `int`
  - `Phosphorus` as `int`
  - `Potassium` as `int`
  - `Temperature` as `float`
  - `Humidity` as `float`
  - `pH_Value` as `float`
  - `Rainfall`as `float`
- Response
  - Success
  ```json
  {
    "input": {
        "Nitrogen": 85,
        "Phosphorus": 28,
        "Potassium": 70,
        "Temperature": 26.5,
        "Humidity": 74.2,
        "pH_Value": 7.0,
        "Rainfall": 500.0
    },
    "predictions": {
        "rotasi_1": [
            {
                "crop": "Blackgram",
                "confidence": 0.8668363690376282
            },
            {
                "crop": "Rice",
                "confidence": 0.04433418810367584
            },
            {
                "crop": "MungBean",
                "confidence": 0.03943661227822304
            }
        ]
    },
    "soil_quality": "Lembap"
  }
  ```
  

#### Prediction-history
- URL : 
  - `/prediction-history?token=`
- Method : 
  - `GET`
- Response
  - Success
  ```json
  {
    "user_id": "cs7n0BriKVl2rHCCIeJ5",
    "total_predictions": 2,
    "history": [
        {
            "input": {
                "Rainfall": 500.0,
                "Temperature": 26.5,
                "pH_Value": 7.0,
                "Potassium": 70,
                "Humidity": 74.2,
                "Nitrogen": 85,
                "Phosphorus": 28
            },
            "predictions": {
                "rotasi_1": [
                    {
                        "crop": "Blackgram",
                        "confidence": 0.8668363690376282
                    },
                    {
                        "crop": "Rice",
                        "confidence": 0.04433418810367584
                    },
                    {
                        "crop": "MungBean",
                        "confidence": 0.03943661227822304
                    }
                ]
            },
            "timestamp": "2024-12-11T13:42:41.562741+00:00",
            "soil_quality": "Lembap",
            "doc_id": "TRPzM5mRKrV0lGmU9OZm"
        },
        {
            "input": {
                "Rainfall": 115.6,
                "Temperature": 20.3,
                "pH_Value": 6.2,
                "Potassium": 77,
                "Humidity": 96.3,
                "Nitrogen": 92,
                "Phosphorus": 14
            },
            "predictions": {
                "rotasi_1": [
                    {
                        "crop": "Rice",
                        "confidence": 0.36330920457839966
                    },
                    {
                        "crop": "Blackgram",
                        "confidence": 0.23600301146507263
                    },
                    {
                        "crop": "MungBean",
                        "confidence": 0.2244139015674591
                    }
                ]
            },
            "timestamp": "2024-12-11T11:56:29.488613+00:00",
            "soil_quality": "Kering",
            "doc_id": "ZaRjavuNxSs3LSNWCnJZ"
        }
    ]
  }
  ```