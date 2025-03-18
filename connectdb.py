import os
from google.cloud import firestore


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/python/api_key.json"


db = firestore.Client(database="exytbdd")

__all__ = ["db"]