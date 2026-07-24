import { Ticket, CheckCircle2, AlertTriangle, Mail } from 'lucide-react';
import styles from './page.module.css';
import TicketsChart from './TicketsChart';
import TicketsPieChart from './TicketsPieChart';
import TopSubjects from './TopSubjects';
import DataSourceInfo from './DataSourceInfo';
import { getServerApiUrl } from '@/utils/api-url';

interface MetricsData {
  total: number;
  by_status: Record<string, number>;
  by_priority: Record<string, number>;
  by_channel: Record<string, number>;
  by_date: Record<string, number>;
  by_subject: Record<string, number>;
}

async function getMetrics(): Promise<MetricsData> {
  const API_URL = getServerApiUrl();
  const response = await fetch(`${API_URL}/metrics/`, { cache: 'no-store' });
  if (!response.ok) throw new Error('Failed to fetch metrics');
  return response.json();
}

export default async function DashboardPage() {
  const metrics = await getMetrics();
  const generatedAt = new Date().toISOString();

  const closed = metrics.by_status['closed'] ?? 0;
  const closedPct = ((closed / metrics.total) * 100).toFixed(1);

  const highPriority = (metrics.by_priority['high'] ?? 0) + (metrics.by_priority['critical'] ?? 0);
  const highPct = ((highPriority / metrics.total) * 100).toFixed(1);

  const topChannel = Object.entries(metrics.by_channel).sort((a, b) => b[1] - a[1])[0];
  const topChannelPct = ((topChannel[1] / metrics.total) * 100).toFixed(0);

  return (
    <main className={styles.dashboard}>
      <section className={styles.header}>
        <h1>Dashboard</h1>
      </section>

      <section className={styles.content}>
        <section className={styles.cards}>
          <article className={styles.card}>
            <div className={styles.cardHeader}>
              <span>Total de tickets</span>
              <Ticket size={20} className={styles.icon} />
            </div>
            <strong>{metrics.total.toLocaleString('pt-BR')}</strong>
            <small>Todos os canais</small>
          </article>

          <article className={styles.card}>
            <div className={styles.cardHeader}>
              <span>Fechados</span>
              <CheckCircle2 size={20} className={styles.iconSuccess} />
            </div>
            <strong>{closed.toLocaleString('pt-BR')}</strong>
            <small>{closedPct}% do total</small>
          </article>

          <article className={styles.card}>
            <div className={styles.cardHeader}>
              <span>Alta prioridade</span>
              <AlertTriangle size={20} className={styles.iconWarning} />
            </div>
            <strong>{highPriority.toLocaleString('pt-BR')}</strong>
            <small>{highPct}% do total</small>
          </article>

          <article className={styles.card}>
            <div className={styles.cardHeader}>
              <span>Canal mais frequente</span>
              <Mail size={20} className={styles.iconPrimary} />
            </div>
            <strong className={styles.capitalize}>{topChannel[0]}</strong>
            <small>{topChannelPct}% do total</small>
          </article>
        </section>

        <section className={styles.chartsGrid}>
          <TicketsChart byDate={metrics.by_date} />
          <TicketsPieChart byChannel={metrics.by_channel} />
        </section>
        <section className={styles.bottomGrid}>
          <TopSubjects bySubject={metrics.by_subject} />
          <DataSourceInfo generatedAt={generatedAt} />
        </section>
      </section>
    </main>
  );
}