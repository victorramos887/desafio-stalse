"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import styles from './header.module.css'

export default function Header() {
  const pathname = usePathname()

  const isTicketsActive = pathname === "/tickets" || pathname.startsWith("/tickets/")
  const isMetricsActive = pathname === "/metrics" || pathname.startsWith("/metrics/")

  return (
    <header className={styles.header}>
      <div className={styles.content}>
        <h1 className={styles.logo}>Mini Inbox</h1>

        <nav className={styles.navigation}>
          <Link
            href="/tickets"
            className={isTicketsActive ? styles.active : ""}
            aria-current={isTicketsActive ? "page" : undefined}
          >
            Tickets
          </Link>
          <Link
            href="/metrics"
            className={isMetricsActive ? styles.active : ""}
            aria-current={isMetricsActive ? "page" : undefined}
          >
            Métricas
          </Link>
        </nav>
      </div>
    </header>
  )
}

