import styles from './header.module.css'

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.content}>
        <h1 className={styles.logo}>Mini Inbox</h1>

        <nav className={styles.navigation}>
          <a href="/tickets">Tickets</a>
          <a href="/metrics">Métricas</a>
        </nav>
      </div>
    </header>
  )
}

