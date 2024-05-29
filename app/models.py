from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from geoalchemy2 import Geography
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "User"
    userId = Column(Integer, primary_key=True, index=True)
    lastname = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Trip(Base):
    __tablename__ = "Trip"
    tripId = Column(Integer, primary_key=True, index=True)
    origin = Column(Geography(geometry_type='POINT', srid=4326), nullable=False)
    destination = Column(Geography(geometry_type='POINT', srid=4326), nullable=False)
    departureTime = Column(TIMESTAMP, nullable=False)

class Payment(Base):
    __tablename__ = "Payment"
    paymentId = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)

class Notification(Base):
    __tablename__ = "Notification"
    notificationId = Column(Integer, primary_key=True, index=True)
    recipientId = Column(Integer, ForeignKey('User.userId'), nullable=False)
    content = Column(String, nullable=False)
    status = Column(String, nullable=False)

class GeoLocation(Base):
    __tablename__ = "GeoLocation"
    locationId = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)#Column(Geography(geometry_type='POINT', srid=4326), nullable=False)

class WebPortal(Base):
    __tablename__ = "WebPortal"
    portalId = Column(Integer, primary_key=True, index=True)
    users = Column(String, nullable=False, default='[]')
    trips = Column(String, nullable=False, default='[]')
    payments = Column(String, nullable=False, default='[]')
    notifications = Column(String, nullable=False, default='[]')