from google.cloud import firestore
from datetime import datetime

class FirestoreLogger:
    def __init__(self):
        self.client = firestore.Client()

    def log_prediction(self, user_id, prediction_data):
        prediction_result = {
            "timestamp": datetime.utcnow(),
            **prediction_data
        }

        ref = self.client.collection('users').document(user_id).collection('history')
        ref.add(prediction_result)
        return prediction_result

    def get_prediction_history(self, user_id):
        try:
            # Ambil semua dokumen history untuk user tertentu
            ref = self.client.collection('users').document(user_id).collection('history')
            docs = ref.order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
            
            # Konversi dokumen ke list
            history = []
            for doc in docs:
                # Ambil data dokumen dan tambahkan ID dokumen
                item = doc.to_dict()
                item['doc_id'] = doc.id
                # Konversi timestamp ke string untuk serialization
                if 'timestamp' in item:
                    item['timestamp'] = item['timestamp'].isoformat()
                history.append(item)
            
            return history
        except Exception as e:
            print(f"Error retrieving prediction history: {e}")
            raise