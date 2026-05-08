export interface Project {
  id: string;
  name: string;
  description: string;
}

export interface Activity {
  id: string;
  projectId: string;
  name: string;
  bac: number;
  plannedProgress: number;
  actualProgress: number;
  actualCost: number;
}

export interface ActivityIndicators {
  pv: number;
  ev: number;
  cv: number;
  sv: number;
  cpi: number | null;
  spi: number | null;
  eac: number | null;
  vac: number | null;
  cpiStatus: string;
  spiStatus: string;
}

export interface ProjectSummary {
  totalBac: number;
  totalPv: number;
  totalEv: number;
  totalAc: number;
  totalCv: number;
  totalSv: number;
  cpi: number | null;
  spi: number | null;
}
