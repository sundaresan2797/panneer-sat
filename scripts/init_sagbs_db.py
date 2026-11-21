"""Run from the project root: python -m scripts.init_sagbs_db"""
from app.services.sagbs_store import init_database

if __name__ == "__main__":
    init_database()
    print("SAGBS enquiry schema is ready.")
