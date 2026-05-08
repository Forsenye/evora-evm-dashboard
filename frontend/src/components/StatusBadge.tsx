interface StatusBadgeProps {
  label: string;
  status: string;
}

export function StatusBadge({ label, status }: StatusBadgeProps) {
  const normalized = status.toLowerCase();
  const colorClass = normalized.includes("eficiencia") || normalized.includes("adelantado")
    ? "bg-green-100 text-green-800"
    : normalized.includes("no calculable")
      ? "bg-gray-100 text-gray-700"
      : normalized.includes("en presupuesto") || normalized.includes("en cronograma")
        ? "bg-blue-100 text-blue-800"
        : "bg-red-100 text-red-800";

  return (
    <span className={`inline-flex rounded-full px-2 py-1 text-xs font-medium ${colorClass}`}>
      {label}: {status}
    </span>
  );
}
