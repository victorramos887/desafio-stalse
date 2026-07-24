'use client';

import {
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';
import styles from './page.module.css';
import { formatWeekLabel, formatWeekTooltip } from '@/utils/dateFormatter';

interface TicketsChartProps {
  byDate: Record<string, number>;
}

function getWeekLabel(dateStr: string): string {
  const d = new Date(dateStr + 'T00:00:00');
  const year = d.getFullYear();
  const startOfYear = new Date(year, 0, 1);
  const week = Math.ceil(
    ((d.getTime() - startOfYear.getTime()) / 86400000 + startOfYear.getDay() + 1) / 7,
  );
  return `${year}-W${String(week).padStart(2, '0')}`;
}

interface ChartDataPoint {
  date: string;
  tickets: number;
  weekLabel: string;
  weekTooltip: string;
}

export default function TicketsChart({ byDate }: TicketsChartProps) {
  const weekMap: Record<string, number> = {};
  for (const [date, count] of Object.entries(byDate)) {
    const week = getWeekLabel(date);
    weekMap[week] = (weekMap[week] ?? 0) + count;
  }

  const data: ChartDataPoint[] = Object.entries(weekMap)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([week, tickets]) => ({ 
      date: week, 
      tickets, 
      weekLabel: formatWeekLabel(week),
      weekTooltip: formatWeekTooltip(week)
    }));

  const CustomTooltip = (props: any) => {
    const { active, payload } = props;
    if (active && payload && payload.length) {
      const dataPoint = payload[0].payload as ChartDataPoint;
      return (
        <div
          style={{
            backgroundColor: '#fff',
            padding: '8px 12px',
            border: '1px solid #ddd',
            borderRadius: '6px',
            fontSize: '13px',
          }}
        >
          <p style={{ margin: 0, fontWeight: 600 }}>{dataPoint.weekTooltip}</p>
          <p style={{ margin: '4px 0 0 0', color: '#2563eb' }}>
            {dataPoint.tickets} tickets
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className={styles.chartCard}>
      <h2 className={styles.chartTitle}>Tickets por dia</h2>
      <ResponsiveContainer width="100%" height={280}>
        <AreaChart data={data} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
          <defs>
            <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#2563eb" stopOpacity={0.3} />
              <stop offset="95%" stopColor="#2563eb" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="#eeeeee" />
          <XAxis
            dataKey="weekLabel"
            tick={{ fontSize: 11, fill: '#6b7280' }}
            tickLine={false}
            axisLine={false}
            interval="preserveStartEnd"
          />
          <YAxis
            tick={{ fontSize: 11, fill: '#6b7280' }}
            tickLine={false}
            axisLine={false}
            width={32}
          />
          <Tooltip content={CustomTooltip} />
          <Area
            type="monotone"
            dataKey="tickets"
            stroke="#2563eb"
            strokeWidth={2}
            fill="url(#colorGradient)"
            dot={false}
            activeDot={{ r: 4 }}
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
