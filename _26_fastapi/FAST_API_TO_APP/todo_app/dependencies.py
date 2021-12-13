from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        # request --> start b --> commit all changes --> save --> close b
