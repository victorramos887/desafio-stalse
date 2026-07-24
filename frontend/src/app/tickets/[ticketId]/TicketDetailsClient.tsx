"use client";

import Link from "next/link";
import { useState } from "react";
import { updateTicket } from "@/services/ticket-service";

import type { Ticket, TicketPriority, TicketStatus } from "@/types/ticket";

import styles from "./page.module.css";

interface TicketDetailsClientProps {
  ticket: Ticket;
  ticketId: string;
}

export default function TicketDetailsClient({
  ticket,
  ticketId,
}: TicketDetailsClientProps) {
  const [status, setStatus] = useState<TicketStatus>(ticket.status);
  const [priority, setPriority] = useState<TicketPriority>(ticket.priority);

  const handleSave = async () => {
    try {
      const updatedTicket = await updateTicket(parseInt(ticketId), {
        status,
        priority,
      });
      console.log("Ticket atualizado com sucesso:", updatedTicket);
    } catch (error) {
      console.error("Erro ao atualizar o ticket:", error);
    }
  }

  return (
    <main className={styles.page}>
      <section className={styles.section}>
        <Link href="/tickets" className={styles.backLink}>
          ← Voltar
        </Link>

        <h1 className={styles.title}>Detalhe do Ticket #{ticketId}</h1>

        <div className={styles.layout}>
          <div className={styles.ticketCard}>
            <div className={styles.infoGrid}>
              <span>customer_name</span>
              <strong>{ticket.customer_name}</strong>

              <span>email</span>
              <p>{ticket.email}</p>

              <span>channel</span>
              <p>{ticket.channel}</p>

              <span>created_at</span>
              <p>{ticket.created_at}</p>

              <span>subject</span>
              <p>{ticket.subject}</p>
            </div>

            <div className={styles.description}>
              <span>description</span>

              <p>{ticket.description}</p>
            </div>

            <div className={styles.divider} />

            <div className={styles.formGroup}>
              <label htmlFor="status">status</label>

              <select
                id="status"
                value={status}
                onChange={(e) => setStatus(e.target.value as TicketStatus)}
              >
                <option value="open">open</option>
                <option value="pending">pending</option>
                <option value="closed">closed</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label htmlFor="priority">priority</label>

              <select
                id="priority"
                value={priority}
                onChange={(e) => setPriority(e.target.value as TicketPriority)}
              >
                <option value="low">low</option>
                <option value="medium">medium</option>
                <option value="high">high</option>
              </select>
            </div>

            <div className={styles.actions}>
              <button className={styles.saveButton} onClick={handleSave}>Salvar alteracao</button>

            </div>
          </div>

          <aside className={styles.summaryCard}>
            <h2>Resumo</h2>

            <div className={styles.summaryItem}>
              <span>ID</span>
              <strong>#{ticketId}</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Canal</span>
              <strong>Email</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Criado em</span>
              <strong>{ticket.created_at}</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Ultima atualizacao</span>
              <strong>{ticket.updated_at}</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Categoria</span>
              <strong>Acesso</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Tags</span>
              <span className={styles.tag}>login</span>
            </div>
          </aside>
        </div>
      </section>
    </main>
  );
}
