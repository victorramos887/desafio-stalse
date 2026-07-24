import type { PaginatedTickets, Ticket, UpdateTicketData } from "@/types/ticket"
import { getClientApiUrl, getServerApiUrl } from "@/utils/api-url"


function getApiUrl(): string {
    return typeof window === "undefined" ? getServerApiUrl() : getClientApiUrl();
}

export class TicketServiceError extends Error {
    status: number;

    constructor(message: string, status: number) {
        super(message);
        this.name = "TicketServiceError";
        this.status = status;
    }
}

async function parseJsonSafely<T>(response: Response): Promise<T> {
    const raw = await response.text();

    if (!raw.trim()) {
        throw new TicketServiceError("Empty response from API", response.status);
    }

    try {
        return JSON.parse(raw) as T;
    } catch {
        throw new TicketServiceError("Invalid JSON response from API", response.status);
    }
}


export async function getTickets(page: number, pageSize: number): Promise<PaginatedTickets> {
    const response = await fetch(`${getApiUrl()}/tickets?page=${page}&page_size=${pageSize}`);

    if (!response.ok) {
        throw new TicketServiceError("Failed to fetch tickets", response.status);
    }
    return parseJsonSafely<PaginatedTickets>(response);
}

export async function getTicketById(ticketId: number): Promise<Ticket> {
    const response = await fetch(`${getApiUrl()}/tickets/${ticketId}`, {
        cache: "no-store",
    });
    
    if (!response.ok) {
        const details = await response.text();
        throw new TicketServiceError(
            `Failed to fetch ticket ${ticketId} (status ${response.status})${details ? `: ${details}` : ""}`,
            response.status,
        );
    }
    return parseJsonSafely<Ticket>(response);
}



export async function updateTicket(ticketId: number, data: UpdateTicketData): Promise<Ticket>  {
    const response = await fetch(`${getApiUrl()}/tickets/${ticketId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)

    });

    if (!response.ok) {
        throw new TicketServiceError("Failed to update ticket", response.status)
    }

    return parseJsonSafely<Ticket>(response);

}
