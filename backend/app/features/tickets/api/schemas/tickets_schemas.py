from pydantic import BaseModel


class SchemaPostTicket(BaseModel):
    customer_name: str
    channel: str
    status: str
    priority: str
