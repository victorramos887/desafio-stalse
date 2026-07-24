import { getTicketById } from "@/services/ticket-service"

import Link from "next/link";

import styles from "./page.module.css";

interface TicketDetailsPageProps {
  params: Promise<{
    ticketId: string;
  }>;
}

export default async function TicketDetailsPage({
  params,
}: TicketDetailsPageProps) {
  const { ticketId } = await params;
  const ticket = await getTicketById(Number(ticketId))

  return (
    <main className={styles.page}>
      <section className={styles.section}>
        <Link href="/tickets" className={styles.backLink}>
          ← Voltar
        </Link>

        <h1 className={styles.title}>
          Detalhe do Ticket #{ticketId}
        </h1>

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

              <p>
                {ticket.description}
              </p>
            </div>

            <div className={styles.divider} />

            <div className={styles.formGroup}>
              <label htmlFor="status">status</label>

              <select id="status" defaultValue={ticket.status}>
                <option value="open">open</option>
                <option value="pending">pending</option>
                <option value="closed">closed</option>
              </select>
            </div>

            <div className={styles.formGroup}>
              <label htmlFor="priority">priority</label>

              <select id="priority" defaultValue={ticket.priority}>
                <option value="low">low</option>
                <option value="medium">medium</option>
                <option value="high">high</option>
              </select>
            </div>

            <div className={styles.actions}>
              <button className={styles.saveButton}>
                Salvar alteração
              </button>

              <button className={styles.closeButton}>
                Fechar ticket
              </button>
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
              <strong>12/05/2025 10:15</strong>
            </div>

            <div className={styles.summaryItem}>
              <span>Última atualização</span>
              <strong>12/05/2025 11:02</strong>
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