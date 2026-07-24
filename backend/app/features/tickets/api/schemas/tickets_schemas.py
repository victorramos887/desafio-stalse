from datetime import datetime

from pydantic import BaseModel


class SchemaPostTicket(BaseModel):
    customer_name: str
    channel: str
    status: str
    priority: str


class TicketEventCreate(BaseModel):
    ticket_id: int
    status: str
    event: str
    created_at: datetime
    source: str
