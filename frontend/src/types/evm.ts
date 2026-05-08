export interface Project {
  id: string;
  name: string;
  description: string | null;
  created_at: string;
  updated_at: string;
}

export interface ProjectCreatePayload {
  name: string;
  description?: string | null;
}

export interface Activity {
  id: string;
  project_id?: string;
  name: string;
  bac: number;
  planned_progress: number;
  actual_progress: number;
  actual_cost: number;
  created_at?: string;
  updated_at?: string;
}

export interface ActivityCreatePayload {
  name: string;
  bac: number;
  planned_progress: number;
  actual_progress: number;
  actual_cost: number;
}

export interface ActivityEvmIndicators {
  pv: number;
  ev: number;
  cv: number;
  sv: number;
  cpi: number | null;
  spi: number | null;
  eac: number | null;
  vac: number | null;
  cost_status: string;
  schedule_status: string;
  bac?: number;
  ac?: number;
}

export interface ActivityWithEvm extends Activity {
  evm: ActivityEvmIndicators;
}

export interface ProjectEvmSummary {
  bac: number;
  pv: number;
  ev: number;
  ac: number;
  cv: number;
  sv: number;
  cpi: number | null;
  spi: number | null;
  eac: number | null;
  vac: number | null;
  cost_status: string;
  schedule_status: string;
}

export interface ProjectEvmSummaryResponse {
  project_id: string;
  project_name: string;
  total_activities: number;
  summary: ProjectEvmSummary;
  activities: ActivityWithEvm[];
  status?: string | null;
}