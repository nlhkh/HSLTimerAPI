from fastapi import APIRouter

from location_services import find_coordinate, Address, Coordinate
from hsl_services import get_routes


router = APIRouter()

@router.get("/coordinateFor")
async def get_coordinate(street: str, city: str, postalCode: str):
    address = Address(street, city, 'Finland', postalCode)
    coordinate = await find_coordinate(address)
    return {
        'lat': coordinate.lat,
        'lon': coordinate.lon
    }

@router.get("/routesForCoordinate")
async def get_routes_for_coordinate(lat: float, lon: float):
    coordinate = Coordinate(lat, lon)
    routes = await get_routes(coordinate)
    return {
        'routes': sorted(routes, key=lambda r: r.arrive_at)
    }

@router.get("/routesForAddress")
async def get_routes_for_address(street: str, city: str, postalCode: str):
    address = Address(street, city, 'Finland', postalCode)
    coordinate = await find_coordinate(address)
    routes = await get_routes(coordinate)
    return {
        'routes': sorted(routes, key=lambda r: r.arrive_at)
    }