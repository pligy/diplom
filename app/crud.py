from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, username):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_id(db: Session, id):
    return db.query(models.User).filter(models.User.userId == id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(lastname=user.lastname, firstname=user.firstname, username=user.username, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    print(db_user.userId)
    db.refresh(db_user)
    return db_user

# Similarly, add CRUD functions for Trip, Payment, Notification, and GeoLocation