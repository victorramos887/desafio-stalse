from pydantic import BaseModel
from datetime import datetime

class SchemaPostTicket(BaseModel):
    customer_name: str
    channel: str
    status: str
    priority: str


class TicketEventCreate(BaseModel):
    ticket_id: int
    status: str
    event: str
    create_at: datetime
    source: str