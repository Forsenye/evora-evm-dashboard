import { FormEvent, useState } from "react";

import { ActivityCreatePayload } from "../types/evm";

interface ActivityFormProps {
  onSubmit: (payload: ActivityCreatePayload) => Promise<void>;
  isSubmitting: boolean;
  disabled: boolean;
}

export function ActivityForm({ onSubmit, isSubmitting, disabled }: ActivityFormProps) {
  const [name, setName] = useState("");
  const [bac, setBac] = useState("");
  const [plannedProgress, setPlannedProgress] = useState("");
  const [actualProgress, setActualProgress] = useState("");
  const [actualCost, setActualCost] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const normalizedName = name.trim();
    const parsedBac = Number(bac);
    const parsedPlanned = Number(plannedProgress);
    const parsedActual = Number(actualProgress);
    const parsedCost = Number(actualCost);

    if (!normalizedName) {
      setError("El nombre de la actividad es obligatorio.");
      return;
    }

    if (!Number.isFinite(parsedBac) || parsedBac <= 0) {
      setError("BAC debe ser mayor que 0.");
      return;
    }

    if (!Number.isFinite(parsedPlanned) || parsedPlanned < 0 || parsedPlanned > 100) {
      setError("El avance planificado debe estar entre 0 y 100.");
      return;
    }

    if (!Number.isFinite(parsedActual) || parsedActual < 0 || parsedActual > 100) {
      setError("El avance real debe estar entre 0 y 100.");
      return;
    }

    if (!Number.isFinite(parsedCost) || parsedCost < 0) {
      setError("El costo actual debe ser mayor o igual que 0.");
      return;
    }

    setError(null);

    await onSubmit({
      name: normalizedName,
      bac: parsedBac,
      planned_progress: parsedPlanned,
      actual_progress: parsedActual,
      actual_cost: parsedCost,
    });

    setName("");
    setBac("");
    setPlannedProgress("");
    setActualProgress("");
    setActualCost("");
  };

  return (
    <form onSubmit={handleSubmit} className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-900">Crear actividad</h2>
      <p className="mt-1 text-sm text-slate-500">
        Registra avance y costos para calcular indicadores EVM automáticamente.
      </p>

      <div className="mt-4 grid gap-3 md:grid-cols-5">
        <div>
          <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="activity-name">
            Nombre
          </label>
          <input
            id="activity-name"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="Diseño de base de datos"
            disabled={disabled}
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="activity-bac">
            BAC
          </label>
          <input
            id="activity-bac"
            type="number"
            min="0"
            step="0.01"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={bac}
            onChange={(event) => setBac(event.target.value)}
            disabled={disabled}
          />
        </div>

        <div>
          <label
            className="mb-1 block text-sm font-medium text-slate-700"
            htmlFor="activity-planned-progress"
          >
            % planificado
          </label>
          <input
            id="activity-planned-progress"
            type="number"
            min="0"
            max="100"
            step="0.01"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={plannedProgress}
            onChange={(event) => setPlannedProgress(event.target.value)}
            disabled={disabled}
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="activity-actual-progress">
            % real
          </label>
          <input
            id="activity-actual-progress"
            type="number"
            min="0"
            max="100"
            step="0.01"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={actualProgress}
            onChange={(event) => setActualProgress(event.target.value)}
            disabled={disabled}
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="activity-actual-cost">
            AC
          </label>
          <input
            id="activity-actual-cost"
            type="number"
            min="0"
            step="0.01"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={actualCost}
            onChange={(event) => setActualCost(event.target.value)}
            disabled={disabled}
          />
        </div>
      </div>

      {error ? <p className="mt-2 text-sm text-rose-600">{error}</p> : null}

      <button
        type="submit"
        disabled={disabled || isSubmitting}
        className="mt-4 rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white disabled:opacity-60"
      >
        {isSubmitting ? "Guardando..." : "Guardar actividad"}
      </button>
    </form>
  );
}