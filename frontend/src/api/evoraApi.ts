import axios from "axios";

import {
  ActivityCreatePayload,
  ActivityWithEvm,
  Project,
  ProjectCreatePayload,
  ProjectEvmSummaryResponse,
} from "../types/evm";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 15000,
});

function getErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const detail = error.response?.data?.detail;
    if (typeof detail === "string") {
      return detail;
    }
    if (error.message) {
      return error.message;
    }
  }

  if (error instanceof Error) {
    return error.message;
  }

  return "Error inesperado al consumir la API de EVORA.";
}

export async function getProjects(): Promise<Project[]> {
  try {
    const response = await apiClient.get<Project[]>("/api/v1/projects");
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}

export async function createProject(payload: ProjectCreatePayload): Promise<Project> {
  try {
    const response = await apiClient.post<Project>("/api/v1/projects", payload);
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}

export async function getProjectById(projectId: string): Promise<Project> {
  try {
    const response = await apiClient.get<Project>(`/api/v1/projects/${projectId}`);
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}

export async function createActivity(
  projectId: string,
  payload: ActivityCreatePayload,
): Promise<ActivityWithEvm> {
  try {
    const response = await apiClient.post<ActivityWithEvm>(
      `/api/v1/projects/${projectId}/activities`,
      payload,
    );
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}

export async function getActivitiesByProject(projectId: string): Promise<ActivityWithEvm[]> {
  try {
    const response = await apiClient.get<ActivityWithEvm[]>(
      `/api/v1/projects/${projectId}/activities`,
    );
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}

export async function getProjectEvmSummary(
  projectId: string,
): Promise<ProjectEvmSummaryResponse> {
  try {
    const response = await apiClient.get<ProjectEvmSummaryResponse>(
      `/api/v1/projects/${projectId}/evm-summary`,
    );
    return response.data;
  } catch (error: unknown) {
    throw new Error(getErrorMessage(error));
  }
}