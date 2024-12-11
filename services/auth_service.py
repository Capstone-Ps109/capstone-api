import requests
from fastapi import HTTPException
from config import AUTH_API_ENDPOINT

def validate_token(token: str):
    try:
        # Debug: Print semua informasi
        print(f"Full Auth Endpoint: {AUTH_API_ENDPOINT}/profile")
        print(f"Token: {token}")

        # Kirim request dengan cara berbeda
        response = requests.get(
            f"{AUTH_API_ENDPOINT}/profile", 
            headers={"Authorization": f"Bearer {token}"},  # Coba dengan header
            params={"token": token}  # Tetap simpan query parameter
        )
        
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.text}")
        
        if response.status_code == 200:
            user_data = response.json()
            return user_data.get('id')
        
        raise HTTPException(status_code=403, detail=f"Token validation failed: {response.text}")
    
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        raise HTTPException(status_code=500, detail=f"Token validation error: {str(e)}")