export function formatDate(dateString: string): string {
  try {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('pt-BR', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
    }).format(date);
  } catch {
    return dateString;
  }
}

export function formatWeekLabel(weekStr: string): string {
  // Converte "2020-W01" para "19 jan" (primeiro dia da semana + mês)
  const match = weekStr.match(/(\d{4})-W(\d{2})/);
  if (!match) return weekStr;

  const [, yearStr, weekNum] = match;
  const year = parseInt(yearStr);
  const week = parseInt(weekNum);

  // ISO 8601: Semana 1 contém 4 de janeiro
  const jan4 = new Date(year, 0, 4);
  const jan4Day = jan4.getDay(); // 0 = domingo, 1 = segunda, ...
  
  // Calcular primeira segunda-feira do ano (semana 1 sempre começa segunda)
  const daysToMonday = jan4Day === 0 ? 6 : jan4Day - 1;
  const weekOneMonday = new Date(jan4.getTime() - daysToMonday * 24 * 60 * 60 * 1000);
  
  // Primeira data da semana desejada
  const weekStart = new Date(weekOneMonday.getTime() + (week - 1) * 7 * 24 * 60 * 60 * 1000);

  const day = String(weekStart.getDate()).padStart(2, '0');
  const month = weekStart.toLocaleDateString('pt-BR', { month: 'short' });

  return `${day} ${month}`;
}

export function formatWeekTooltip(weekStr: string): string {
  // Converte "2020-W01" para "01 de dez de 2023" (primeiro dia da semana completo)
  const match = weekStr.match(/(\d{4})-W(\d{2})/);
  if (!match) return weekStr;

  const [, yearStr, weekNum] = match;
  const year = parseInt(yearStr);
  const week = parseInt(weekNum);

  // ISO 8601: Semana 1 contém 4 de janeiro
  const jan4 = new Date(year, 0, 4);
  const jan4Day = jan4.getDay();
  
  // Calcular primeira segunda-feira do ano (semana 1 sempre começa segunda)
  const daysToMonday = jan4Day === 0 ? 6 : jan4Day - 1;
  const weekOneMonday = new Date(jan4.getTime() - daysToMonday * 24 * 60 * 60 * 1000);
  
  // Primeira data da semana desejada
  const weekStart = new Date(weekOneMonday.getTime() + (week - 1) * 7 * 24 * 60 * 60 * 1000);

  return new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
  }).format(weekStart);
}
