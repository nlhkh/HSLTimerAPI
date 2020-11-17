from typing import Optional

from fastapi import FastAPI

from location_services import find_coordinate, Address, Coordinate
from hsl_services import get_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {
        'message': "Welcome to HSL Timer API"
    }

@app.get("/coordinateFor")
async def get_coordinate(street: str, city: str, postalCode: str):
    address = Address(street, city, 'Finland', postalCode)
    coordinate = await find_coordinate(address)
    return {
        'lat': coordinate.lat,
        'lon': coordinate.lon
    }

@app.get("/routesForCoordinate")
async def get_routes_for_coordinate(lat: float, lon: float):
    coordinate = Coordinate(lat, lon)
    routes = await get_routes(coordinate)
    return {
        'routes': routes
    }
