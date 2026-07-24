import styles from './page.module.css'

interface TicketDetailsPageProps {
    params: Promise<{
        ticketId: string
    }>
}


export default async function TicketDetailsPage({params }:TicketDetailsPageProps) {

    const { ticketId } = await params;

    return (
        <main className={styles.page}>
        <section className={styles.section}>
            <h1>Detalhes do ticket</h1>

            <p>Ticket ID: {ticketId}</p>
        </section>
        </main>
    )
    

}