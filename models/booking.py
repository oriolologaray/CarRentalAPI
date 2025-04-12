from datetime import datetime

from pydantic import BaseModel


class Booking(BaseModel):
    id: str
    start_time: datetime
    end_time: datetime
    bookerId: str

    def is_active(self):
        return self.start_time <= datetime.now() <= self.end_time