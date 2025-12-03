from sqlalchemy import Column, Integer, Float, String, JSON, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class LocationRecord(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    accuracy = Column(Float)
    altitude = Column(Float)
    speed = Column(Float)
    timestamp = Column(Integer)
    cell_info = Column(JSON)

engine = create_engine("sqlite:///data.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
