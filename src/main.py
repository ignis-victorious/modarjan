#  ________________
#  Import LIBRARIES
from typing import Any, Generator, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

#  Import FILES
from .models import DBHero, Hero
#  ________________


# SQLAlchemy model
Base: Any = declarative_base()

# FastAPI app
app: FastAPI = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine: Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Dependency
def get_session() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a Hero
@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)) -> DBHero:
    db_hero = DBHero(**hero.model_dump())
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


# Read all heroes
@app.get("/heroes/", response_model=list[Hero])
def read_heroes(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
) -> List[DBHero]:
    heroes = session.query(DBHero).offset(skip).limit(limit).all()
    return heroes


# Read a hero by ID
@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)) -> DBHero:
    hero: DBHero | None = session.query(DBHero).filter(DBHero.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


# Update a Hero
@app.put("/heroes/{hero_id}", response_model=Hero)
def update_hero(
    hero_id: int, hero_data: Hero, session: Session = Depends(get_session)
) -> DBHero:
    hero: DBHero | None = session.query(DBHero).filter(DBHero.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    # Update the hero's attributes
    for field, value in hero_data.model_dump().items():
        setattr(hero, field, value)

    session.commit()
    session.refresh(hero)
    return hero


# Delete a Hero
@app.delete("/heroes/{hero_id}", response_model=Hero)
def delete_hero(hero_id: int, session: Session = Depends(get_session)) -> DBHero:
    hero: DBHero | None = session.query(DBHero).filter(DBHero.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return hero


#  ________________
#  Import LIBRARIES
#  Import FILES
#  ________________
