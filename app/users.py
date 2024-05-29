from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine
from models import GeoLocation
from sqlalchemy import func
from fastapi import Request

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return crud.create_user(db=db, user=user)

@router.get("/users/{id}", response_model=schemas.User)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate = Body(..., media_type="application/json"), db: Session = Depends(get_db)):
    print(f"Received user data: {user}")
    print(f"Received user data: {user.username}")
    db_user = crud.get_user(db, username=user.username)
    print(db_user)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = crud.create_user(db=db, user=user)
    print(f"Created user: {new_user}")
    return new_user


@router.post("/save-location/", response_model=schemas.GeoLocation)
def save_location(data: dict, db: Session = Depends(get_db)):
    try:
        # Создаем новый объект GeoLocation, используя модель из models.py
        new_location = models.GeoLocation(**data)
        db.add(new_location)
        db.commit()
        db.refresh(new_location)

        # Возвращаем данные в формате схемы
        return schemas.GeoLocation.from_orm(new_location)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-locations/")
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(
        GeoLocation.locationId,
        GeoLocation.location
    ).all()
    return {
        "locations": [{"locationId": loc.locationId, "location": loc.location} for loc in locations]
    }
