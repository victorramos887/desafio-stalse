import { getTicketById, TicketServiceError } from "@/services/ticket-service";
import { notFound } from "next/navigation";
import TicketDetailsClient from "./TicketDetailsClient";

interface TicketDetailsPageProps {
  params: {
    ticketId: string;
  } | Promise<{
    ticketId: string;
  }>;
}

export default async function TicketDetailsPage({
  params,
}: TicketDetailsPageProps) {
  const { ticketId } = await Promise.resolve(params);
  const parsedId = Number(ticketId);

  if (!Number.isInteger(parsedId) || parsedId <= 0) {
    notFound();
  }

  try {
    const ticket = await getTicketById(parsedId);

    return <TicketDetailsClient ticket={ticket} ticketId={ticketId} />;
  } catch (error) {
    if (error instanceof TicketServiceError && error.status === 404) {
      notFound();
    }

    throw error;
  }
}