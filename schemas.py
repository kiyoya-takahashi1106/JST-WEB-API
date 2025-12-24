from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservationRequest(BaseModel):
    uid: str
    organizer_name: str
    title: str
    event_place: Optional[str] = None
    event_from_at: Optional[datetime] = None
    event_to_at: Optional[datetime] = None
    details: Optional[str] = None
    sns: Optional[str] = None
    sns_id: Optional[str] = None
    display_place: str
    display_from_at: datetime
    display_to_at: datetime
