from uuid import uuid4

import time

from cache import  set_cache, get_cache, delete_cache

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserResponse




# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User API with Redis Caching")


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "User API is running"}


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        id=str(uuid4()),
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    delete_cache("users")

    return new_user


@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    # Check Redis cache
    cached_users = get_cache("users")

    if cached_users is not None:
        print("CACHE HIT")
        return cached_users

    print("CACHE MISS")

    # Get users from MySQL
    users = db.query(User).all()

    # Convert users to JSON
    users_data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        }
        for user in users
    ]

    # Store in Redis for 60 seconds
    set_cache("users", users_data, expire=60)

    return users_data

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: str,
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.age = user.age

    db.commit()
    db.refresh(existing_user)

    # Invalidate users cache
    delete_cache("users")

    return existing_user

@app.delete("/users/{user_id}")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(existing_user)
    db.commit()

    # Invalidate users cache
    delete_cache("users")

    return {"message": "User deleted successfully"}

@app.get("/performance-test")
def performance_test(db: Session = Depends(get_db)):

    # MySQL timing
    start = time.perf_counter()

    users = db.query(User).all()

    mysql_time = time.perf_counter() - start

    # Redis timing
    start = time.perf_counter()

    cached_users = get_cache("users")

    redis_time = time.perf_counter() - start

    return {
        "mysql_time_seconds": mysql_time,
        "redis_time_seconds": redis_time,
        "redis_faster": redis_time < mysql_time
    }