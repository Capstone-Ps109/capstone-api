import os
import logging
from google.cloud import storage
from google.oauth2 import service_account
from google.auth import default

GOOGLE_APPLICATION_CREDENTIALS = "C:/Users/User/AppData/Roaming/gcloud/application_default_credentials.json"

logging.basicConfig(level=logging.INFO)

def get_credentials():
    try:
        # Coba file service account terlebih dahulu
        credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        
        if credentials_path and os.path.exists(credentials_path):
            logging.info(f"Menggunakan file service account: {credentials_path}")
            return service_account.Credentials.from_service_account_file(credentials_path)
        
        # Jika gagal, gunakan kredensial default
        logging.info("Beralih ke kredensial default")
        credentials, _ = default()
        return credentials
    
    except Exception as e:
        logging.error(f"Kesalahan pengambilan kredensial: {e}")
        raise ValueError("Tidak dapat mengambil kredensial Google Cloud")

def download_model(bucket_name='model-api109', model_path='model-prod/optimized_model.tflite', output_path='downloads/optimized_model.tflite'):
    try:
        credentials = get_credentials()
        
        logging.info(f"Mencoba download model dari {bucket_name}/{model_path}")
        
        storage_client = storage.Client(
            project='plantro-project', 
            credentials=credentials
        )
        
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(model_path)
        
        if not bucket.exists():
            raise ValueError(f"Bucket {bucket_name} tidak ditemukan.")
        if not blob.exists():
            raise ValueError(f"File {model_path} tidak ditemukan di bucket {bucket_name}.")
        
        # Pastikan direktori tujuan ada
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        blob.download_to_filename(output_path)
        
        logging.info(f"Model berhasil didownload ke {output_path}")
    
    except Exception as e:
        logging.error(f"Gagal download model: {e}")
        raise

# Tambahan fungsi untuk debug
def list_bucket_contents(bucket_name='model-api109'):
    try:
        credentials = get_credentials()
        storage_client = storage.Client(
            project='plantro-project', 
            credentials=credentials
        )
        
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs()
        
        print("Isi Bucket:")
        for blob in blobs:
            print(blob.name)
    
    except Exception as e:
        logging.error(f"Gagal list bucket contents: {e}")
        raise