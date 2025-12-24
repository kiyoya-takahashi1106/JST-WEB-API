from pydantic import BaseModel
from datetime import datetime

class ReservationRequest(BaseModel):
    uid: str
    organizer_name: str
    title: str
    event_place: str
    event_from_at: datetime
    event_to_at: datetime
    details: str
    sns: str
    sns_id: str
    display_place: str
    display_from_at: datetime
    display_to_at: datetime
