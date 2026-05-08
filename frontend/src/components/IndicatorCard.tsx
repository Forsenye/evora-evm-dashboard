interface IndicatorCardProps {
  title: string;
  value: number | null;
}

export function IndicatorCard({ title, value }: IndicatorCardProps) {
  const formattedValue = value === null ? "N/A" : value.toFixed(2);

  return (
    <article className="rounded-lg bg-white p-4 shadow">
      <h3 className="text-sm font-semibold text-gray-500">{title}</h3>
      <p className="mt-2 text-2xl font-bold text-gray-900">{formattedValue}</p>
    </article>
  );
}
