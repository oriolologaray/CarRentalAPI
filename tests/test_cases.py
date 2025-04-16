BOOKING_REQUEST_BODY = {
    "carId": "car-02",
    "startDate": "1999-01-01",
    "endDate": "2000-01-01",
    "bookerId": "person-04"
}

BOOKING_REQUEST_INVALID_DATES_BODY = {
    "carId": "car-01",
    "startDate": "2025-01-01",
    "endDate": "2025-01-31",
    "bookerId": "person-01"
}

BOOKING_REQUEST_INVALID_CAR_BODY = {
    "carId": "car-99",
    "startDate": "2024-01-01",
    "endDate": "2026-01-01",
    "bookerId": "person-01"
}
