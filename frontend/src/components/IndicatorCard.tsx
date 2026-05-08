import { formatCurrency, formatNumber, formatPercentage } from "../utils/formatters";
import { StatusBadge } from "./StatusBadge";

interface IndicatorCardProps {
  label: string;
  value: number | null;
  format: "currency" | "number" | "percentage";
  status?: string;
  helperText?: string;
}

function formatValue(value: number | null, format: IndicatorCardProps["format"]): string {
  if (format === "currency") {
    return formatCurrency(value);
  }

  if (format === "percentage") {
    return formatPercentage(value);
  }

  return formatNumber(value);
}

export function IndicatorCard({ label, value, format, status, helperText }: IndicatorCardProps) {
  return (
    <article className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">{label}</p>
      <p className="mt-2 text-2xl font-bold text-slate-900">{formatValue(value, format)}</p>
      {helperText ? <p className="mt-1 text-xs text-slate-500">{helperText}</p> : null}
      {status ? (
        <div className="mt-3">
          <StatusBadge status={status} />
        </div>
      ) : null}
    </article>
  );
}