import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

interface EvmChartData {
  activityName: string;
  pv: number;
  ev: number;
  ac: number;
}

interface EvmChartProps {
  data: EvmChartData[];
}

export function EvmChart({ data }: EvmChartProps) {
  return (
    <section className="rounded-lg bg-white p-4 shadow">
      <h2 className="mb-3 text-lg font-semibold">Comparacion PV, EV y AC</h2>
      <div className="h-80 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="activityName" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="pv" fill="#3b82f6" name="PV" />
            <Bar dataKey="ev" fill="#10b981" name="EV" />
            <Bar dataKey="ac" fill="#f97316" name="AC" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}
