import TicketsTable from "@/components/tickets-table/tickets-table"
import styles from "./page.module.css"

export default function TicketsPage() {
  return (
    <main className={styles.page}>
      <section className={styles.section}>
        <h1>Tickets</h1>

        <TicketsTable />
      </section>
    </main>
  );
}

