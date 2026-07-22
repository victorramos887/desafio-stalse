from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.get(
    "/",
    status_code = status.HTTP_200_OK,
)
async def get_tickets():
    return {
        "tickets": [
            {"id": 1, "title": "Ticket 1", "description": "Description for ticket 1"},
            {"id": 2, "title": "Ticket 2", "description": "Description for ticket 2"}
        ]
    }