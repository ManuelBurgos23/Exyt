from google.cloud import firestore

db = firestore.Client()

def add_user():
    doc_ref = db.collection("usuarios").document("usuario1")
    doc_ref.set({"nombre":"Pedro","edad":18})
    print("Usuario añadido")

add_user()
