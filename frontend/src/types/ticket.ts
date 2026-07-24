export type TicketStatus = "open" | "closed" | "pending";
export type TicketPriority = "low" | "medium" | "high";

export interface Ticket {
    id: number;
    customer_name: string;
    channel: string;
    status: TicketStatus;
    priority: TicketPriority;
    created_at: string;
    updated_at: string;
    description: string;
    subject: string;
    email: string;
}


export interface UpdateTicketData {
    status?: TicketStatus;
    priority?: TicketPriority;
}

export interface PaginatedTickets {
    items: Ticket[];
    page: number;
    page_size: number;
    total_items: number;
    total_pages: number;
}
