from sqlalchemy import Integer, Float, String, DateTime, Text, create_engine, Column, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Tenant(Base):
    __tablename__  = "tenants"
    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    gender = Column(String(7))
    email = Column(String(60))
    
class Property(Base):
    __tablename__="properties"
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    location = Column(String(50), nullable=False)
    house_num = Column(String(7))
    rent_amount = Column(Float(10,4))
    
class RentalContract(Base):
    __tablename__="rental_contracts"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))
    start_date = Column(DateTime)
    
    tenant = relationship("Tenant", backref="contracts")
    property = relationship("Property", backref="contracts")
    
engine = create_engine("sqlite:///rentals.db", echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# Base.metadata.create_all(bind=engine)
