"use client";

import { useEffect } from "react";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <html lang="pt-br">
      <body style={{ fontFamily: "var(--font-poppins)", padding: "2rem" }}>
        <h2>Algo deu errado</h2>
        <p>Tente recarregar a pagina.</p>
        <button type="button" onClick={() => reset()}>
          Tentar novamente
        </button>
      </body>
    </html>
  );
}
