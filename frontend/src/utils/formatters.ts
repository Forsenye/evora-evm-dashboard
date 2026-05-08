export function formatCurrency(value: number | null): string {
  if (value === null) {
    return "No calculable";
  }

  return new Intl.NumberFormat("es-CO", {
    style: "currency",
    currency: "COP",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

export function formatNumber(value: number | null): string {
  if (value === null) {
    return "No calculable";
  }

  return new Intl.NumberFormat("es-CO", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

export function formatPercentage(value: number | null): string {
  if (value === null) {
    return "No calculable";
  }

  return `${formatNumber(value)}%`;
}