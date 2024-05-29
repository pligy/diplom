from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    lastname: str
    firstname: str
    username: str
    password: str
    role: str

class User(UserCreate):
    userId: int

    class Config:
        from_attributes = True
        #orm_mode = True

class TripBase(BaseModel):
    origin: str
    destination: str
    departureTime: str

class Trip(TripBase):
    tripId: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    amount: float
    status: str

class Payment(PaymentBase):
    paymentId: int

    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    recipientId: int
    content: str
    status: str

class Notification(NotificationBase):
    notificationId: int

    class Config:
        orm_mode = True

class GeoLocationBase(BaseModel):
    location: str

class GeoLocation(GeoLocationBase):
    #locationId: int

    class Config:
        from_attributes = True
        #orm_mode = True

class WebPortalBase(BaseModel):
    users: List[str]
    trips: List[str]
    payments: List[str]
    notifications: List[str]

class WebPortal(WebPortalBase):
    portalId: int

    class Config:
        orm_mode = True