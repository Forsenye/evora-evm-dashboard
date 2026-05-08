interface StatusBadgeProps {
  status: string;
}

const STATUS_CLASS_MAP: Record<string, string> = {
  "Eficiente en costos": "bg-emerald-100 text-emerald-800 border-emerald-200",
  "En presupuesto": "bg-sky-100 text-sky-800 border-sky-200",
  "Sobre presupuesto": "bg-rose-100 text-rose-800 border-rose-200",
  Adelantado: "bg-emerald-100 text-emerald-800 border-emerald-200",
  "En cronograma": "bg-sky-100 text-sky-800 border-sky-200",
  Atrasado: "bg-amber-100 text-amber-800 border-amber-200",
  "No calculable": "bg-slate-100 text-slate-700 border-slate-200",
};

export function StatusBadge({ status }: StatusBadgeProps) {
  const className = STATUS_CLASS_MAP[status] ?? "bg-slate-100 text-slate-700 border-slate-200";

  return (
    <span className={`inline-flex rounded-full border px-2 py-1 text-xs font-medium ${className}`}>
      {status}
    </span>
  );
}