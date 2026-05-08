import { ActivityWithEvm } from "../types/evm";
import { formatCurrency, formatNumber, formatPercentage } from "../utils/formatters";
import { StatusBadge } from "./StatusBadge";

interface ActivityTableProps {
  activities: ActivityWithEvm[];
}

export function ActivityTable({ activities }: ActivityTableProps) {
  if (activities.length === 0) {
    return (
      <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
        <h2 className="text-lg font-semibold text-slate-900">Actividades</h2>
        <p className="mt-2 text-sm text-slate-500">
          Este proyecto aún no tiene actividades registradas.
        </p>
      </section>
    );
  }

  return (
    <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-900">Actividades</h2>
      <div className="mt-3 overflow-x-auto">
        <table className="min-w-full border-collapse text-sm">
          <thead>
            <tr className="text-left text-slate-600">
              <th className="border-b p-2">Actividad</th>
              <th className="border-b p-2">BAC</th>
              <th className="border-b p-2">Avance planificado</th>
              <th className="border-b p-2">Avance real</th>
              <th className="border-b p-2">AC</th>
              <th className="border-b p-2">PV</th>
              <th className="border-b p-2">EV</th>
              <th className="border-b p-2">CV</th>
              <th className="border-b p-2">SV</th>
              <th className="border-b p-2">CPI</th>
              <th className="border-b p-2">SPI</th>
              <th className="border-b p-2">EAC</th>
              <th className="border-b p-2">VAC</th>
              <th className="border-b p-2">Estado costo</th>
              <th className="border-b p-2">Estado cronograma</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity.id} className="align-top">
                <td className="border-b p-2 font-medium text-slate-900">{activity.name}</td>
                <td className="border-b p-2">{formatCurrency(activity.bac)}</td>
                <td className="border-b p-2">{formatPercentage(activity.planned_progress)}</td>
                <td className="border-b p-2">{formatPercentage(activity.actual_progress)}</td>
                <td className="border-b p-2">{formatCurrency(activity.actual_cost)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.pv)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.ev)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.cv)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.sv)}</td>
                <td className="border-b p-2">{formatNumber(activity.evm.cpi)}</td>
                <td className="border-b p-2">{formatNumber(activity.evm.spi)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.eac)}</td>
                <td className="border-b p-2">{formatCurrency(activity.evm.vac)}</td>
                <td className="border-b p-2">
                  <StatusBadge status={activity.evm.cost_status} />
                </td>
                <td className="border-b p-2">
                  <StatusBadge status={activity.evm.schedule_status} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}