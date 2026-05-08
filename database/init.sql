CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(150) NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS activities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    bac NUMERIC(14, 2) NOT NULL CHECK (bac > 0),
    planned_progress NUMERIC(5, 2) NOT NULL CHECK (planned_progress >= 0 AND planned_progress <= 100),
    actual_progress NUMERIC(5, 2) NOT NULL CHECK (actual_progress >= 0 AND actual_progress <= 100),
    actual_cost NUMERIC(14, 2) NOT NULL CHECK (actual_cost >= 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_activities_project_id ON activities(project_id);
