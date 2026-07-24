import styles from './page.module.css';

interface DataSourceInfoProps {
  generatedAt: string;
}

export default function DataSourceInfo({ generatedAt }: DataSourceInfoProps) {
  return (
    <aside className={styles.dataSourceCard}>
      <h2 className={styles.dataSourceTitle}>Fonte dos dados</h2>

      <pre className={styles.dataSourceCode}>
{`{
  "source": "/metrics",
  "dataset": "Kaggle",
  "provider": "suraj520/customer-support-ticket-dataset",
  "generated_at": "${generatedAt}"
}`}
      </pre>

      <p className={styles.dataSourceHint}>Dados processados via ETL e servidos por /metrics.</p>
    </aside>
  );
}
