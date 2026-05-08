# EVORA MVP Delivery Notes

## Release

- Version: `v1.0.0`
- Tag: `v1.0.0`
- Branch: `release/v1.0.0`
- Date: `2026-05-08`

## Included scope

- FastAPI backend with OpenAPI (`/api-docs.json`) and Swagger UI (`/swagger-ui`).
- EVM calculation service with activity and project summary metrics.
- Project CRUD endpoints.
- Activity CRUD endpoints.
- Project EVM summary endpoint.
- React + Vite dashboard with EVM indicators and chart.
- Backend tests and frontend production build validation.
- Technical documentation and AI-assisted process documentation.

## Validation status

- Backend tests: `64 passed`.
- Frontend build: `successful`.
- MVP ready for release handoff from `release/v1.0.0` to `main`.

## Out of scope in this release

- Cloud deployment configuration.
- AWS, EC2, Terraform, Kubernetes, CI/CD.
- Authentication, roles and notification workflows.

## Corporate environment restrictions

- The MVP is designed for local execution with Python, Node.js, npm, browser access and localhost ports.
- Some corporate environments may restrict shell usage, script execution, dependency installation, browser localhost access or frontend-backend communication.
- No attempt was made to bypass corporate security controls.
- Final demo should be executed from an authorized environment that allows local runtime prerequisites.
