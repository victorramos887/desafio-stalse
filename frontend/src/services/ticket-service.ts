import type { Ticket } from "@/types/ticket"

const API_URL = 
    process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";


export async function getTickets(): Promise<Ticket[]> {
    const response = await fetch(`${API_URL}/tickets`);

    if (!response.ok) {
        throw new Error("Failed to fetch tickets");
    }
    return response.json();
}

export async function getTicketById(ticketId: number): Promise<Ticket> {
    const response = await fetch(`${API_URL}/tickets/${ticketId}`);
    
    if (!response.ok) {
        throw new Error("Failed to fetch ticket");
    }
    return response.json();
}


export async function updateTicketStatus(ticketId: number, status: string): Promise<Ticket> {
    const response = await fetch(`${API_URL}/tickets/${ticketId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ status }),
    });

    if (!response.ok) {
        throw new Error("Failed to update ticket status");
    }
    return response.json();
}