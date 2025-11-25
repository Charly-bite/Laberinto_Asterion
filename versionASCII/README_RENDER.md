# Deploying to Render.com (scaffold)

This folder contains a minimal Flask scaffold to iterate on converting the ASCII game into a web app.

Quick steps to deploy on Render using the Dockerfile:

1. Push this repository to a Git provider (GitHub/GitLab).
2. Create a new Render service → "Web Service" and connect your repo.
3. Choose "Docker" as the environment and point Render to the folder `versionASCII` (the Dockerfile is located there).
4. Set the port to `5000` (Render sets $PORT automatically but we bind to 5000 inside container).
5. Deploy — the scaffold exposes `/` (UI), `/api/start` and `/api/action`.

Next steps (recommended):
- Implement a headless controller for `LaberintoAsterionASCII` (refactor input() uses), then wire it into `/api/start` and `/api/action` to run game logic server-side per session.
- Add persistent session storage (Redis) if you want sessions to survive restarts.
- Harden worker/process settings and set a sensible `--workers` value depending on traffic.
