from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import users#, trips, payments, notifications
from database import engine
import models

# Initialize database models
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include API routers
app.include_router(users.router)
# app.include_router(trips.router)
# app.include_router(payments.router)
# app.include_router(notifications.router)

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/auth/registration")
async def reg_form(request: Request):
    return templates.TemplateResponse("reg_form.html", {"request": request})

@app.get("/lk")
async def lk(request: Request):
    return templates.TemplateResponse("lk.html", {"request": request})