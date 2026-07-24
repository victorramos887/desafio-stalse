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
              <span>Nome do Cliente</span>
              <strong>{ticket.customer_name}</strong>

              <span>Email</span>
              <p>{ticket.email}</p>

              <span>Canal</span>
              <p>{ticket.channel}</p>

              <span>Criado em</span>
              <p>{ticket.created_at}</p>

              <span>Assunto</span>
              <p>{ticket.subject}</p>
            </div>

            <div className={styles.description}>
              <span>Descrição</span>

              <p>{ticket.description}</p>
            </div>

            <div className={styles.divider} />

            <div className={styles.formGroup}>
              <label htmlFor="status">Status</label>

              <select
                id="status"
                value={status}
                onChange={(e) => setStatus(e.target.value as TicketStatus)}
              >
                <option value="open">Aberto</option>
                <option value="pending">Pendente</option>
                <option value="closed">Fechado</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label htmlFor="priority">Prioridade</label>

              <select
                id="priority"
                value={priority}
                onChange={(e) => setPriority(e.target.value as TicketPriority)}
              >
                <option value="low">Baixo</option>
                <option value="medium">Médio</option>
                <option value="high">Alto</option>
              </select>
            </div>

            <div className={styles.actions}>
              <button className={styles.saveButton} onClick={handleSave}>Salvar alteração</button>

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
