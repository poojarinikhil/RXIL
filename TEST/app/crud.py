from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # Add password hashing in production
    db_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_entity(db: Session, entity_id: int):
    return db.query(models.Entity).filter(models.Entity.id == entity_id).first()

def get_entities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Entity).offset(skip).limit(limit).all()

def create_entity(db: Session, entity: schemas.EntityCreate):
    db_entity = models.Entity(**entity.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

def delete_entity(db: Session, entity_id: int):
    entity = db.query(models.Entity).filter(models.Entity.id == entity_id).first()
    db.delete(entity)
    db.commit()
    return entity

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_entity(db: Session, entity_id: int, entity: schemas.EntityCreate):
    db_entity = db.query(models.Entity).filter(models.Entity.id == entity_id).first()
    for key, value in entity.dict().items():
        setattr(db_entity, key, value)
    db.commit()
    db.refresh(db_entity)
    return db_entity
