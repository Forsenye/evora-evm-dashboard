import { useEffect, useMemo, useState } from "react";

import {
  createActivity,
  createProject,
  getProjectById,
  getProjectEvmSummary,
  getProjects,
} from "../api/evoraApi";
import { ActivityForm } from "../components/ActivityForm";
import { ActivityTable } from "../components/ActivityTable";
import { EvmChart } from "../components/EvmChart";
import { IndicatorCard } from "../components/IndicatorCard";
import { ProjectForm } from "../components/ProjectForm";
import { StatusBadge } from "../components/StatusBadge";
import {
  ActivityCreatePayload,
  Project,
  ProjectCreatePayload,
  ProjectEvmSummaryResponse,
} from "../types/evm";

export function Dashboard() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [selectedProjectId, setSelectedProjectId] = useState<string>("");
  const [summary, setSummary] = useState<ProjectEvmSummaryResponse | null>(null);

  const [isProjectsLoading, setIsProjectsLoading] = useState(true);
  const [isSummaryLoading, setIsSummaryLoading] = useState(false);
  const [isCreatingProject, setIsCreatingProject] = useState(false);
  const [isCreatingActivity, setIsCreatingActivity] = useState(false);

  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const selectedProject = useMemo(
    () => projects.find((project) => project.id === selectedProjectId) ?? null,
    [projects, selectedProjectId],
  );

  const loadProjects = async (preferredProjectId?: string) => {
    setIsProjectsLoading(true);
    setErrorMessage(null);

    try {
      const items = await getProjects();
      setProjects(items);

      if (items.length === 0) {
        setSelectedProjectId("");
        setSummary(null);
        return;
      }

      if (preferredProjectId && items.some((project) => project.id === preferredProjectId)) {
        setSelectedProjectId(preferredProjectId);
        return;
      }

      setSelectedProjectId((currentId) => {
        if (currentId && items.some((project) => project.id === currentId)) {
          return currentId;
        }

        return items[0].id;
      });
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "No fue posible cargar proyectos.";
      setErrorMessage(message);
      setProjects([]);
      setSelectedProjectId("");
      setSummary(null);
    } finally {
      setIsProjectsLoading(false);
    }
  };

  const loadSummary = async (projectId: string) => {
    setIsSummaryLoading(true);
    setErrorMessage(null);

    try {
      const [summaryResponse] = await Promise.all([
        getProjectEvmSummary(projectId),
        getProjectById(projectId),
      ]);
      setSummary(summaryResponse);
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "No fue posible cargar el resumen EVM.";
      setErrorMessage(message);
      setSummary(null);
    } finally {
      setIsSummaryLoading(false);
    }
  };

  useEffect(() => {
    void loadProjects();
  }, []);

  useEffect(() => {
    if (!selectedProjectId) {
      return;
    }

    void loadSummary(selectedProjectId);
  }, [selectedProjectId]);

  const handleCreateProject = async (payload: ProjectCreatePayload) => {
    setIsCreatingProject(true);
    setErrorMessage(null);

    try {
      const created = await createProject(payload);
      await loadProjects(created.id);
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "No fue posible crear el proyecto.";
      setErrorMessage(message);
    } finally {
      setIsCreatingProject(false);
    }
  };

  const handleCreateActivity = async (payload: ActivityCreatePayload) => {
    if (!selectedProjectId) {
      setErrorMessage("Selecciona un proyecto antes de registrar actividades.");
      return;
    }

    setIsCreatingActivity(true);
    setErrorMessage(null);

    try {
      await createActivity(selectedProjectId, payload);
      await loadSummary(selectedProjectId);
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "No fue posible crear la actividad.";
      setErrorMessage(message);
    } finally {
      setIsCreatingActivity(false);
    }
  };

  return (
    <main className="mx-auto flex min-h-screen w-full max-w-7xl flex-col gap-4 p-4">
      <header className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <h1 className="text-3xl font-bold text-slate-900">EVORA</h1>
        <p className="mt-2 text-sm text-slate-600">
          Plataforma inteligente para seguimiento de proyectos con Valor Ganado.
        </p>
      </header>

      <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
        <h2 className="text-lg font-semibold text-slate-900">Proyectos</h2>

        {isProjectsLoading ? <p className="mt-2 text-sm text-slate-500">Cargando proyectos...</p> : null}

        {!isProjectsLoading && projects.length === 0 ? (
          <p className="mt-2 text-sm text-slate-500">
            Aún no hay proyectos. Crea el primer proyecto para iniciar el seguimiento EVM.
          </p>
        ) : null}

        {!isProjectsLoading && projects.length > 0 ? (
          <div className="mt-3 max-w-md">
            <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="project-selector">
              Proyecto activo
            </label>
            <select
              id="project-selector"
              className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
              value={selectedProjectId}
              onChange={(event) => setSelectedProjectId(event.target.value)}
            >
              {projects.map((project) => (
                <option key={project.id} value={project.id}>
                  {project.name}
                </option>
              ))}
            </select>
          </div>
        ) : null}
      </section>

      <ProjectForm onSubmit={handleCreateProject} isSubmitting={isCreatingProject} />

      <ActivityForm
        onSubmit={handleCreateActivity}
        isSubmitting={isCreatingActivity}
        disabled={!selectedProjectId}
      />

      {errorMessage ? (
        <section className="rounded-lg border border-rose-200 bg-rose-50 p-3 text-sm text-rose-700">
          {errorMessage}
        </section>
      ) : null}

      {!selectedProjectId ? (
        <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <p className="text-sm text-slate-500">
            Selecciona o crea un proyecto para visualizar su análisis EVM.
          </p>
        </section>
      ) : null}

      {selectedProjectId && isSummaryLoading ? (
        <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <p className="text-sm text-slate-500">Cargando resumen EVM del proyecto...</p>
        </section>
      ) : null}

      {selectedProjectId && !isSummaryLoading && summary ? (
        <>
          <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
            <h2 className="text-lg font-semibold text-slate-900">Resumen del proyecto</h2>
            <p className="mt-1 text-sm text-slate-600">{selectedProject?.name ?? summary.project_name}</p>
            <p className="text-sm text-slate-500">Actividades registradas: {summary.total_activities}</p>
            {summary.status ? <p className="mt-2 text-sm text-slate-500">{summary.status}</p> : null}
          </section>

          <section className="grid gap-3 md:grid-cols-2 lg:grid-cols-4">
            <IndicatorCard
              label="BAC total"
              value={summary.summary.bac}
              format="currency"
              helperText="Budget at Completion"
            />
            <IndicatorCard
              label="PV total"
              value={summary.summary.pv}
              format="currency"
              helperText="Planned Value"
            />
            <IndicatorCard
              label="EV total"
              value={summary.summary.ev}
              format="currency"
              helperText="Earned Value"
            />
            <IndicatorCard
              label="AC total"
              value={summary.summary.ac}
              format="currency"
              helperText="Actual Cost"
            />
            <IndicatorCard label="CV" value={summary.summary.cv} format="currency" />
            <IndicatorCard label="SV" value={summary.summary.sv} format="currency" />
            <IndicatorCard
              label="CPI"
              value={summary.summary.cpi}
              format="number"
              status={summary.summary.cost_status}
            />
            <IndicatorCard
              label="SPI"
              value={summary.summary.spi}
              format="number"
              status={summary.summary.schedule_status}
            />
            <IndicatorCard label="EAC" value={summary.summary.eac} format="currency" />
            <IndicatorCard label="VAC" value={summary.summary.vac} format="currency" />
          </section>

          <section className="flex flex-wrap gap-2 rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
            <StatusBadge status={summary.summary.cost_status} />
            <StatusBadge status={summary.summary.schedule_status} />
          </section>

          <ActivityTable activities={summary.activities} />
          <EvmChart activities={summary.activities} />

          {summary.activities.length === 0 ? (
            <section className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
              <p className="text-sm text-slate-500">
                Este proyecto aún no tiene actividades registradas.
              </p>
            </section>
          ) : null}
        </>
      ) : null}
    </main>
  );
}