from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    interest = Column(String(200), nullable=False)

    def __init__(self, name, email, telefone, latitude, longitude, temperature, interest):
        self.name = name
        self.email = email
        self.telefone = telefone
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.interest = interest

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'telefone': self.telefone,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'temperature': self.temperature,
            'interest': self.interest
        }
