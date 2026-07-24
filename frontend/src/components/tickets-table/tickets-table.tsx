import styles from "./ticket-table.module.css"

export default function TicketsTable() {
    return (
        <div className={styles.container}>
            <table className={styles.table}>
                <thead>
                    <tr>
                        <th>Cliente</th>
                        <th>Canal</th>
                        <th>Status</th>
                        <th>Prioridade</th>
                        <th>Criado em</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Maria Silva</td>
                        <td>WhatsApp</td>
                        <td>Open</td>
                        <td>High</td>
                        <td>24/07/2026</td>
                    </tr>
                </tbody>

            </table>

        </div>
    )
}