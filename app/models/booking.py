from datetime import date

from pydantic import BaseModel, Field, model_validator


class Booking(BaseModel):
    id: str | None = None
    car_id: str = Field(alias='carId')
    start_date: date = Field(alias='startDate')
    end_date: date = Field(alias='endDate')
    booker_id: str = Field(alias='bookerId')

    @model_validator(mode='after')
    def check_start_date_before_end_date(self) -> 'Booking':
        if self.start_date >= self.end_date:
            raise ValueError("startDate must be before endDate")
        return self

    def is_active_on(self, rental_date: date, end_rental_date: date = None) -> bool:
        # If end_rental_date is passed as a parameter, the function will check if there is overlap between ranges.
        if end_rental_date:
            return self.start_date <= rental_date and end_rental_date <= self.end_date

        # Else check that the booking is not active for that single day.
        return self.start_date <= rental_date <= self.end_date
