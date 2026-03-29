# Copilot Instructions for techlearning ✅

Purpose: Help AI coding agents be immediately productive by explaining the repo structure, runtime & debug steps, conventions, and file-level examples found in this project.

## Quick facts 🧭
- Framework: **Flask 3** (see `requirements.txt`).
- Entry point: `src/app.py` — app created with `create_app()` and run when executed directly.
- Blueprints live in `src/features/<feature>/` (example: `src/features/user/users.py`).
- Config: `src/config.py` exposes a `Config` class loaded with `app.config.from_object(Config)`.

## Quick start (local) ⚡
1. Create a virtual env and install deps:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   python src/app.py
   # => server available at http://127.0.0.1:5000
   ```

3. Example requests:

   ```bash
   curl http://127.0.0.1:5000/api/users         # GET list
   curl -X POST -H "Content-Type: application/json" -d '{"name":"Sam"}' http://127.0.0.1:5000/api/users
   curl http://127.0.0.1:5000/api/users/1       # GET by id
   curl -X DELETE http://127.0.0.1:5000/api/users/1
   ```

## Architecture & patterns (what to know) 🔧
- App assembly: `create_app()` in `src/app.py` creates the Flask app and **registers blueprints**. All new features should follow the blueprint pattern and be registered there.
- Blueprint convention: Feature modules expose a blueprint object (e.g., `user_bp` in `src/features/user/users.py`). When adding new features, follow the same pattern and keep routes inside the feature folder.
- URL structure: `app.register_blueprint(user_bp, url_prefix="/api")` — all feature routes are served under `/api`.
- In-memory state: `src/features/user/users.py` uses an in-memory list `users = [...]` and mutates it directly (global variable). Note: restarting the server resets state.
- Response patterns: Endpoints commonly return JSON using `jsonify()` with a shape like `{ "success": True, "message": "...", "data": ... }`, though some endpoints return the direct resource (see `get_user`). Stay consistent with existing endpoints when adding new routes.
- ID allocation: New resources are created with `id = len(users) + 1`. Follow or improve this logic for new in-memory endpoints, but prefer a persistent store for production code.

## Files of interest (examples) 📁
- `src/app.py` — app factory and blueprint registration.
- `src/config.py` — minimal `Config` class (DEBUG = True).
- `src/features/user/users.py` — concrete example of a feature blueprint, route handlers and JSON conventions.
- `src/features/student/student_api.py` — placeholder showing where student logic would live (currently empty).
- `requirements.txt` — external dependencies (note: includes LLM/AI libs like `langchain`, `openai` which are present but unused by current code).

## Developer conventions & notes ✍️
- Keep feature code inside `src/features/<feature>/` with a single module (or package) per feature.
- Name blueprints with `<feature>_bp` and import them in `src/app.py` for registration.
- Use JSON request/response patterns consistent with `users.py`.
- Linting/format: `autopep8` and `pycodestyle` are available in dependencies; use them to match style.

## Debugging tips 🐞
- Run `python src/app.py` to start the dev server (Config.DEBUG is True by default).
- Place breakpoints in feature modules (VSCode will hit them once the server imports the modules and routes are invoked).
- Because data is in-memory, reproduce issues by sending the same sequence of requests during a single process run.

## Integration & external deps ⚠️
- The repo contains heavy LLM-related dependencies (`langchain`, `openai`, etc.) in `requirements.txt`. These are *not* referenced in the current code — confirm the intended usage before adding LLM-based features.
- There is no database dependency or external service configured; adding persistent storage requires modifying the app factory and likely introducing configuration in `src/config.py`.

## Tests & CI 🔍
- There are currently **no tests** or CI configs in the repo. When adding tests, add `tests/` and prefer `pytest`.

---
If anything in this doc is unclear or you want more detail (examples for adding a new feature or a sample test), tell me which part to expand and I'll iterate. ✅
