import styles from './page.module.css';

interface TopSubjectsProps {
  bySubject: Record<string, number>;
}

function toLabel(value: string): string {
  if (!value) return '-';
  return value
    .split(' ')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

export default function TopSubjects({ bySubject }: TopSubjectsProps) {
  const items = Object.entries(bySubject)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5);

  if (!items.length) return null;

  const maxCount = items[0][1] || 1;

  return (
    <section className={styles.topSubjectsCard}>
      <h2 className={styles.topSubjectsTitle}>Top assuntos</h2>
      <div className={styles.topSubjectsList}>
        {items.map(([subject, count]) => {
          const widthPercent = Math.max(12, Math.round((count / maxCount) * 100));
          return (
            <div key={subject} className={styles.topSubjectRow}>
              <span className={styles.topSubjectName}>{toLabel(subject)}</span>
              <div className={styles.topSubjectBarTrack}>
                <div className={styles.topSubjectBarFill} style={{ width: `${widthPercent}%` }} />
              </div>
              <strong className={styles.topSubjectValue}>{count}</strong>
            </div>
          );
        })}
      </div>
    </section>
  );
}
