from datetime import datetime

from pydantic import BaseModel


class SchemaPostTicket(BaseModel):
    customer_name: str
    channel: str
    status: str
    priority: str
    email: str
    subject: str
    description: str


class TicketEventCreate(BaseModel):
    ticket_id: int
    status: str
    event: str
    created_at: datetime
    source: str
    
    
    
# class TicketDetails(BaseModel):
#     customer_name: str
#     channel: str
#     status: str
#     priority: str
#     description: str
#     subject: str
