'use client';

import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from 'recharts';
import styles from './page.module.css';

interface TicketsPieChartProps {
  byChannel: Record<string, number>;
}

interface PieDataPoint {
  name: string;
  value: number;
}

const COLORS = ['#2563eb', '#0ea5e9', '#14b8a6', '#f59e0b', '#ef4444', '#8b5cf6'];

function toLabel(value: string): string {
  if (!value) return '-';
  return value
    .split(' ')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

export default function TicketsPieChart({ byChannel }: TicketsPieChartProps) {
  const data: PieDataPoint[] = Object.entries(byChannel)
    .map(([name, value]) => ({ name: toLabel(name), value }))
    .sort((a, b) => b.value - a.value);

  if (!data.length) {
    return (
      <section className={styles.chartCard}>
        <h2 className={styles.chartTitle}>Distribuicao por canal</h2>
        <p className={styles.emptyChart}>Sem dados para exibir.</p>
      </section>
    );
  }

  return (
    <section className={styles.chartCard}>
      <h2 className={styles.chartTitle}>Distribuicao por canal</h2>
      <div className={styles.pieLayout}>
        <ResponsiveContainer width="100%" height={260}>
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              innerRadius={56}
              outerRadius={88}
              paddingAngle={2}
              labelLine={false}
            >
              {data.map((entry, index) => (
                <Cell key={entry.name} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip
              formatter={(value) => [`${value ?? 0} ticket(s)`, 'Quantidade']}
            />
          </PieChart>
        </ResponsiveContainer>

        <div className={styles.pieLegend}>
          {data.map((item, index) => (
            <div key={item.name} className={styles.pieLegendItem}>
              <span
                className={styles.pieLegendColor}
                style={{ backgroundColor: COLORS[index % COLORS.length] }}
              />
              <span className={styles.pieLegendLabel}>{item.name}</span>
              <strong className={styles.pieLegendValue}>{item.value}</strong>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
