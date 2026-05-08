import { useState } from "react";

interface ActivityFormProps {
  onSubmit: (payload: {
    name: string;
    bac: number;
    plannedProgress: number;
    actualProgress: number;
    actualCost: number;
  }) => void;
}

export function ActivityForm({ onSubmit }: ActivityFormProps) {
  const [name, setName] = useState("");
  const [bac, setBac] = useState(0);
  const [plannedProgress, setPlannedProgress] = useState(0);
  const [actualProgress, setActualProgress] = useState(0);
  const [actualCost, setActualCost] = useState(0);

  return (
    <form
      className="rounded-lg bg-white p-4 shadow"
      onSubmit={(event) => {
        event.preventDefault();
        onSubmit({ name, bac, plannedProgress, actualProgress, actualCost });
      }}
    >
      <h2 className="mb-3 text-lg font-semibold">Actividad</h2>
      <div className="grid gap-3 md:grid-cols-5">
        <input
          className="rounded border border-gray-300 px-3 py-2"
          placeholder="Nombre"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        <input
          className="rounded border border-gray-300 px-3 py-2"
          type="number"
          placeholder="BAC"
          value={bac}
          onChange={(event) => setBac(Number(event.target.value))}
        />
        <input
          className="rounded border border-gray-300 px-3 py-2"
          type="number"
          placeholder="% plan"
          value={plannedProgress}
          onChange={(event) => setPlannedProgress(Number(event.target.value))}
        />
        <input
          className="rounded border border-gray-300 px-3 py-2"
          type="number"
          placeholder="% real"
          value={actualProgress}
          onChange={(event) => setActualProgress(Number(event.target.value))}
        />
        <input
          className="rounded border border-gray-300 px-3 py-2"
          type="number"
          placeholder="AC"
          value={actualCost}
          onChange={(event) => setActualCost(Number(event.target.value))}
        />
      </div>
      <button
        type="submit"
        className="mt-3 rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white"
      >
        Guardar actividad
      </button>
    </form>
  );
}
