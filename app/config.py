from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CARS_DB_PATH = BASE_DIR / "app" / "data" / "cars.json"
BOOKINGS_DB_PATH = BASE_DIR / "app" / "data" / "bookings.json"
