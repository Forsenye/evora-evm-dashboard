import { Activity, ActivityIndicators } from "../types/evm";
import { StatusBadge } from "./StatusBadge";

interface ActivityTableRow {
  activity: Activity;
  indicators: ActivityIndicators;
}

interface ActivityTableProps {
  rows: ActivityTableRow[];
}

export function ActivityTable({ rows }: ActivityTableProps) {
  return (
    <div className="overflow-x-auto rounded-lg bg-white p-4 shadow">
      <h2 className="mb-3 text-lg font-semibold">Actividades</h2>
      <table className="min-w-full border-collapse text-sm">
        <thead>
          <tr className="text-left text-gray-600">
            <th className="border-b p-2">Actividad</th>
            <th className="border-b p-2">BAC</th>
            <th className="border-b p-2">PV</th>
            <th className="border-b p-2">EV</th>
            <th className="border-b p-2">AC</th>
            <th className="border-b p-2">CV</th>
            <th className="border-b p-2">SV</th>
            <th className="border-b p-2">CPI</th>
            <th className="border-b p-2">SPI</th>
            <th className="border-b p-2">Estados</th>
          </tr>
        </thead>
        <tbody>
          {rows.map(({ activity, indicators }) => (
            <tr key={activity.id}>
              <td className="border-b p-2">{activity.name}</td>
              <td className="border-b p-2">{activity.bac.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.pv.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.ev.toFixed(2)}</td>
              <td className="border-b p-2">{activity.actualCost.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.cv.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.sv.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.cpi === null ? "N/A" : indicators.cpi.toFixed(2)}</td>
              <td className="border-b p-2">{indicators.spi === null ? "N/A" : indicators.spi.toFixed(2)}</td>
              <td className="border-b p-2">
                <div className="flex flex-col gap-1">
                  <StatusBadge label="CPI" status={indicators.cpiStatus} />
                  <StatusBadge label="SPI" status={indicators.spiStatus} />
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
