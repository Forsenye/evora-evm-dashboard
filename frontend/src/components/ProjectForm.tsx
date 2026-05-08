import { useState } from "react";

interface ProjectFormProps {
  onSubmit: (payload: { name: string; description: string }) => void;
}

export function ProjectForm({ onSubmit }: ProjectFormProps) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  return (
    <form
      className="rounded-lg bg-white p-4 shadow"
      onSubmit={(event) => {
        event.preventDefault();
        onSubmit({ name, description });
      }}
    >
      <h2 className="mb-3 text-lg font-semibold">Proyecto</h2>
      <div className="grid gap-3 md:grid-cols-2">
        <input
          className="rounded border border-gray-300 px-3 py-2"
          placeholder="Nombre del proyecto"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        <input
          className="rounded border border-gray-300 px-3 py-2"
          placeholder="Descripcion"
          value={description}
          onChange={(event) => setDescription(event.target.value)}
        />
      </div>
      <button
        type="submit"
        className="mt-3 rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white"
      >
        Guardar proyecto
      </button>
    </form>
  );
}
