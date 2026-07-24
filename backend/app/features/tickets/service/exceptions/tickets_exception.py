class TicketNotFoundException(Exception):
    def __init__(self, ticket_id: int):
        super().__init__(f"Ticket with ID {ticket_id} not found.")
