'use client'

import { useEffect, useMemo, useState } from 'react';
import { getTickets } from '@/services/ticket-service';
import type { Ticket } from '@/types/ticket'
import { ArrowBigDownDashIcon } from 'lucide-react';

import styles from "./ticket-table.module.css"

type TicketFilters = {
    customer_name: string;
    channel: string;
    status: string;
    priority: string;
    created_at: string;
}

type SortDirection = "asc" | "desc";

export default function TicketsTable() {

    // CONSTANTES
    const [tickets, setTickets] = useState<Ticket[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [showFilters, setShowFilters] = useState(false);
    const [createdAtSort, setCreatedAtSort] = useState<SortDirection>("asc");
    const [filters, setFilters] = useState<TicketFilters>({
        customer_name: "",
        channel: "",
        status: "",
        priority: "",
        created_at: "",
    });

    const statusClass: Record<string, string> = {
        open: styles.open,
        closed: styles.closed,
        pending: styles.pending,
    }

    const priorityClass: Record<string, string> = {
        low: styles.low,
        medium: styles.medium,
        high: styles.high,
    }

    function handleFilterChange(field: keyof TicketFilters, value: string) {
        setFilters((prev) => ({ ...prev, [field]: value }));
    }

    function extractDate(value: string): string {
        const match = value.match(/\d{4}-\d{2}-\d{2}/);
        return match ? match[0] : "";
    }

    function handleCreatedAtSort() {
        setCreatedAtSort((prev) => (prev === "asc" ? "desc" : "asc"));
    }

    const filteredTickets = useMemo(() => {
        const filtered = tickets.filter((ticket) => {
            const customerMatch = ticket.customer_name
                .toLowerCase()
                .includes(filters.customer_name.toLowerCase());
            const channelMatch = ticket.channel
                .toLowerCase()
                .includes(filters.channel.toLowerCase());
            const statusMatch = filters.status
                ? ticket.status.toLowerCase() === filters.status.toLowerCase()
                : true;
            const priorityMatch = filters.priority
                ? ticket.priority.toLowerCase() === filters.priority.toLowerCase()
                : true;
            const dateMatch = filters.created_at
                ? extractDate(ticket.created_at) === filters.created_at
                : true;

            return customerMatch && channelMatch && statusMatch && priorityMatch && dateMatch;
        });

        const sorted = [...filtered].sort((left, right) => {
            const leftTimestamp = Date.parse(left.created_at);
            const rightTimestamp = Date.parse(right.created_at);

            if (!Number.isNaN(leftTimestamp) && !Number.isNaN(rightTimestamp)) {
                return createdAtSort === "asc"
                    ? leftTimestamp - rightTimestamp
                    : rightTimestamp - leftTimestamp;
            }

            const leftDate = extractDate(left.created_at);
            const rightDate = extractDate(right.created_at);
            return createdAtSort === "asc"
                ? leftDate.localeCompare(rightDate)
                : rightDate.localeCompare(leftDate);
        });

        return sorted;
    }, [tickets, filters, createdAtSort]);

    useEffect(() => {
        async function loadTickets() {
            try {
                const data = await getTickets();
                setTickets(data);
            } catch (_error) {
                setError("Failed to load tickets");
            } finally {
                setLoading(false);
            }
        }
        loadTickets();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div className={styles.container}>
            <div className={styles.tableActions}>
                <button
                    type="button"
                    className={styles.toggleFiltersButton}
                    onClick={() => setShowFilters((prev) => !prev)}
                >
                    {showFilters ? "Ocultar filtros" : "Mostrar filtros"}
                </button>
            </div>
            <table className={styles.table}>
                <thead>
                    <tr>
                        <th>Cliente</th>
                        <th>Canal</th>
                        <th>Status</th>
                        <th>Prioridade</th>
                        <th>
                            <button
                                type="button"
                                className={styles.sortButton}
                                onClick={handleCreatedAtSort}
                            >
                                Criado em {createdAtSort === "asc" ? "↑" : "↓"}
                            </button>
                        </th>
                        <th>Ação</th>
                    </tr>
                    {showFilters && <tr>
                        <th>
                            <input
                                className={styles.filterInput}
                                value={filters.customer_name}
                                onChange={(event) => handleFilterChange("customer_name", event.target.value)}
                                placeholder="Filtrar"
                            />
                        </th>
                        <th>
                            <input
                                className={styles.filterInput}
                                value={filters.channel}
                                onChange={(event) => handleFilterChange("channel", event.target.value)}
                                placeholder="Filtrar"
                            />
                        </th>
                        <th>
                            <select
                                className={styles.filterInput}
                                value={filters.status}
                                onChange={(event) => handleFilterChange("status", event.target.value)}
                            >
                                <option value="">Todos</option>
                                <option value="open">Open</option>
                                <option value="pending">Pending</option>
                                <option value="closed">Closed</option>
                            </select>
                        </th>
                        <th>
                            <select
                                className={styles.filterInput}
                                value={filters.priority}
                                onChange={(event) => handleFilterChange("priority", event.target.value)}
                            >
                                <option value="">Todos</option>
                                <option value="low">Low</option>
                                <option value="medium">Medium</option>
                                <option value="high">High</option>
                            </select>
                        </th>
                        <th>
                            <input
                                className={styles.filterInput}
                                type="date"
                                value={filters.created_at}
                                onChange={(event) => handleFilterChange("created_at", event.target.value)}
                            />
                        </th>
                        <th />
                    </tr>}
                </thead>
                <tbody>
                    {filteredTickets.map((ticket) => (
                        <tr key={ticket.id}>
                            <td>{ticket.customer_name}</td>
                            <td>{ticket.channel}</td>
                            <td className={statusClass[ticket.status]}>{ticket.status}</td>
                            <td className={priorityClass[ticket.priority]}>{ticket.priority}</td>
                            <td>{ticket.created_at}</td>
                            <td><button type="button"><ArrowBigDownDashIcon /></button></td>
                        </tr>
                    ))}
                </tbody>

            </table>

        </div>
    )
}