type TicketStatus = "open" | "closed" | "pending";
type TicketPriority = "low" | "medium" | "high";

export interface Ticket {
    id: number;
    customer_name: string;
    channel: string;
    status: TicketStatus;
    priority: TicketPriority;
    created_at: string;
}