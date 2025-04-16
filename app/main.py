from fastapi import FastAPI

from app.routes import cars_route, bookings_route

app = FastAPI()

app.include_router(cars_route.router)
app.include_router(bookings_route.router)
