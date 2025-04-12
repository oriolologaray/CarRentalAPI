from fastapi import FastAPI

from routes import cars_route

app = FastAPI()

app.include_router(cars_route.router)