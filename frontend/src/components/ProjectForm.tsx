import { FormEvent, useState } from "react";

import { ProjectCreatePayload } from "../types/evm";

interface ProjectFormProps {
  onSubmit: (payload: ProjectCreatePayload) => Promise<void>;
  isSubmitting: boolean;
}

export function ProjectForm({ onSubmit, isSubmitting }: ProjectFormProps) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const normalizedName = name.trim();
    if (!normalizedName) {
      setError("El nombre del proyecto es obligatorio.");
      return;
    }

    setError(null);
    await onSubmit({
      name: normalizedName,
      description: description.trim() ? description.trim() : null,
    });

    setName("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit} className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-900">Crear proyecto</h2>
      <p className="mt-1 text-sm text-slate-500">Registra un proyecto para iniciar el análisis EVM.</p>

      <div className="mt-4 grid gap-3 md:grid-cols-2">
        <div>
          <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="project-name">
            Nombre
          </label>
          <input
            id="project-name"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="Implementación EVORA"
          />
        </div>

        <div>
          <label
            className="mb-1 block text-sm font-medium text-slate-700"
            htmlFor="project-description"
          >
            Descripción
          </label>
          <input
            id="project-description"
            className="w-full rounded-md border border-slate-300 px-3 py-2 text-sm"
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            placeholder="Opcional"
          />
        </div>
      </div>

      {error ? <p className="mt-2 text-sm text-rose-600">{error}</p> : null}

      <button
        type="submit"
        disabled={isSubmitting}
        className="mt-4 rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white disabled:opacity-60"
      >
        {isSubmitting ? "Guardando..." : "Guardar proyecto"}
      </button>
    </form>
  );
}