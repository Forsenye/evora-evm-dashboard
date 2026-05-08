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

import { ActivityWithEvm } from "../types/evm";

interface EvmChartProps {
  activities: ActivityWithEvm[];
}

export function EvmChart({ activities }: EvmChartProps) {
  if (activities.length === 0) {
    return (
      <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
        <h2 className="text-lg font-semibold text-slate-900">Comparación PV, EV y AC</h2>
        <p className="mt-2 text-sm text-slate-500">
          No hay datos de actividades para graficar.
        </p>
      </section>
    );
  }

  const data = activities.map((activity) => ({
    activityName: activity.name,
    pv: activity.evm.pv,
    ev: activity.evm.ev,
    ac: activity.actual_cost,
  }));

  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-900">Comparación PV, EV y AC</h2>
      <div className="mt-3 h-80 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="activityName" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="pv" fill="#2563eb" name="PV" />
            <Bar dataKey="ev" fill="#16a34a" name="EV" />
            <Bar dataKey="ac" fill="#f97316" name="AC" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}