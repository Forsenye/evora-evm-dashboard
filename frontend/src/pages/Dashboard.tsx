import { ActivityForm } from "../components/ActivityForm";
import { ActivityTable } from "../components/ActivityTable";
import { EvmChart } from "../components/EvmChart";
import { IndicatorCard } from "../components/IndicatorCard";
import { ProjectForm } from "../components/ProjectForm";
import { StatusBadge } from "../components/StatusBadge";
import { Activity, ActivityIndicators, Project, ProjectSummary } from "../types/evm";

const mockProject: Project = {
  id: "1",
  name: "MVP EVORA",
  description: "Plataforma para seguimiento con EVM",
};

const mockActivities: Activity[] = [
  {
    id: "a1",
    projectId: "1",
    name: "Analisis de requerimientos",
    bac: 3000,
    plannedProgress: 100,
    actualProgress: 100,
    actualCost: 2800,
  },
  {
    id: "a2",
    projectId: "1",
    name: "Construccion backend",
    bac: 5000,
    plannedProgress: 70,
    actualProgress: 60,
    actualCost: 3600,
  },
  {
    id: "a3",
    projectId: "1",
    name: "Construccion frontend",
    bac: 4000,
    plannedProgress: 50,
    actualProgress: 35,
    actualCost: 1600,
  },
];

function interpretCpi(cpi: number | null): string {
  if (cpi === null) {
    return "CPI no calculable cuando AC = 0";
  }
  if (cpi > 1) {
    return "eficiencia en costos";
  }
  if (cpi === 1) {
    return "en presupuesto";
  }
  return "sobre presupuesto";
}

function interpretSpi(spi: number | null): string {
  if (spi === null) {
    return "SPI no calculable cuando PV = 0";
  }
  if (spi > 1) {
    return "adelantado";
  }
  if (spi === 1) {
    return "en cronograma";
  }
  return "atrasado";
}

function calculateActivityIndicators(activity: Activity): ActivityIndicators {
  const pv = (activity.plannedProgress / 100) * activity.bac;
  const ev = (activity.actualProgress / 100) * activity.bac;
  const cv = ev - activity.actualCost;
  const sv = ev - pv;
  const cpi = activity.actualCost === 0 ? null : ev / activity.actualCost;
  const spi = pv === 0 ? null : ev / pv;
  const eac = cpi === null || cpi === 0 ? null : activity.bac / cpi;
  const vac = eac === null ? null : activity.bac - eac;

  return {
    pv,
    ev,
    cv,
    sv,
    cpi,
    spi,
    eac,
    vac,
    cpiStatus: interpretCpi(cpi),
    spiStatus: interpretSpi(spi),
  };
}

function calculateSummary(rows: { activity: Activity; indicators: ActivityIndicators }[]): ProjectSummary {
  const totalBac = rows.reduce((sum, row) => sum + row.activity.bac, 0);
  const totalPv = rows.reduce((sum, row) => sum + row.indicators.pv, 0);
  const totalEv = rows.reduce((sum, row) => sum + row.indicators.ev, 0);
  const totalAc = rows.reduce((sum, row) => sum + row.activity.actualCost, 0);
  const totalCv = totalEv - totalAc;
  const totalSv = totalEv - totalPv;
  const cpi = totalAc === 0 ? null : totalEv / totalAc;
  const spi = totalPv === 0 ? null : totalEv / totalPv;

  return { totalBac, totalPv, totalEv, totalAc, totalCv, totalSv, cpi, spi };
}

export function Dashboard() {
  const rows = mockActivities.map((activity) => ({
    activity,
    indicators: calculateActivityIndicators(activity),
  }));

  const summary = calculateSummary(rows);

  const chartData = rows.map(({ activity, indicators }) => ({
    activityName: activity.name,
    pv: indicators.pv,
    ev: indicators.ev,
    ac: activity.actualCost,
  }));

  return (
    <main className="mx-auto flex max-w-7xl flex-col gap-4 p-4">
      <header className="rounded-lg bg-white p-4 shadow">
        <h1 className="text-2xl font-bold">EVORA Dashboard</h1>
        <p className="mt-1 text-gray-600">{mockProject.name}</p>
        <p className="text-sm text-gray-500">{mockProject.description}</p>
      </header>

      <ProjectForm onSubmit={(payload) => console.log("Project payload", payload)} />
      <ActivityForm onSubmit={(payload) => console.log("Activity payload", payload)} />

      <section className="grid gap-3 md:grid-cols-3 lg:grid-cols-6">
        <IndicatorCard title="Total BAC" value={summary.totalBac} />
        <IndicatorCard title="Total PV" value={summary.totalPv} />
        <IndicatorCard title="Total EV" value={summary.totalEv} />
        <IndicatorCard title="Total AC" value={summary.totalAc} />
        <IndicatorCard title="CPI" value={summary.cpi} />
        <IndicatorCard title="SPI" value={summary.spi} />
      </section>

      <section className="flex flex-wrap gap-2">
        <StatusBadge label="CPI" status={interpretCpi(summary.cpi)} />
        <StatusBadge label="SPI" status={interpretSpi(summary.spi)} />
      </section>

      <ActivityTable rows={rows} />
      <EvmChart data={chartData} />
    </main>
  );
}
