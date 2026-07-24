import type { Ticket, UpdateTicketData } from "@/types/ticket"


const API_URL = 
    process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export class TicketServiceError extends Error {
    status: number;

    constructor(message: string, status: number) {
        super(message);
        this.name = "TicketServiceError";
        this.status = status;
    }
}


export async function getTickets(): Promise<Ticket[]> {
    const response = await fetch(`${API_URL}/tickets`);

    if (!response.ok) {
        throw new Error("Failed to fetch tickets");
    }
    return response.json();
}

export async function getTicketById(ticketId: number): Promise<Ticket> {
    const response = await fetch(`${API_URL}/tickets/${ticketId}`, {
        cache: "no-store",
    });
    
    if (!response.ok) {
        const details = await response.text();
        throw new TicketServiceError(
            `Failed to fetch ticket ${ticketId} (status ${response.status})${details ? `: ${details}` : ""}`,
            response.status,
        );
    }
    return response.json();
}



export async function updateTicket(ticketId: number, data: UpdateTicketData): Promise<Ticket>  {
    const response = await fetch(`${API_URL}/tickets/${ticketId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)

    });

    if (!response.ok) {
        throw new Error("Failed to update ticket")
    }

    return response.json();

}