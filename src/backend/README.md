# SyntaxSentinels Source Code

This folder contains the **source code** for the SyntaxSentinels backend, built with Python and Flask.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Setting Up the Virtual Environment](#setting-up-the-virtual-environment)
   - [Windows](#windows)
   - [Linux-and-macOS](#linux-and-macos)
4. [Installing Dependencies](#installing-dependencies)
5. [Environment Variables](#environment-variables)
6. [Running the Server](#running-the-server)

---

## Project Overview

- The backend runs on **Flask**.
- Auth0 is used for authentication (`AUTH0_DOMAIN`, `AUTH0_AUDIENCE`, etc. in your environment variables).
- Common tasks include:
  - Activating a virtual environment.
  - Installing Python packages from `requirements.txt`.
  - Starting the Flask development server.

---

## Prerequisites

- **Python 3.7+** (check via `python --version`).
- A compatible shell (Command Prompt, PowerShell on Windows, or a standard terminal on Linux/macOS).

---

## Setting Up the Virtual Environment

1. **Navigate** to the backend directory:

   ```bash
   cd backend
   ```

2. **Create** the virtual environment (named `.venv`):
   ```bash
   python -m venv .venv
   ```

### Windows

- **Command Prompt**:
  ```bash
  .venv\Scripts\activate.bat
  ```
- **PowerShell**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### Linux and macOS

```bash
source .venv/bin/activate
```

Once activated, your terminal prompt should prefix with `(.venv)` or similar.

---

## Installing Dependencies

Make sure you are **inside** the activated `.venv` environment, then run:

```bash
pip install -r requirements.txt
```

_(Note: the previous command was `pip install -m requirements.txt`; typically it should be `-r` for installing from a file.)_

---

## Environment Variables

Create a `.env` file or otherwise set these variables in your environment. Below is a table describing each:

| **Variable**      | **Description**                                                           | **Example/Default** |
| ----------------- | ------------------------------------------------------------------------- | ------------------- |
| `FLASK_ENV`       | Sets the Flask environment mode. Typically `development` or `production`. | `development`       |
| `PORT`            | The port on which the Flask app listens.                                  | `5000`              |
| `AUTH0_DOMAIN`    | Your Auth0 tenant domain, e.g. `your-tenant.us.auth0.com`.                | _(none)_            |
| `AUTH0_AUDIENCE`  | The Auth0 audience for your API.                                          | _(none)_            |
| `AUTH0_CLIENT_ID` | The Auth0 Client ID used by the app.                                      | _(none)_            |
| `APP_NAME`        | The name of your application.                                             | `SyntaxSentinels`   |

Example `.env`:

```
FLASK_ENV=development
PORT=5000
AUTH0_DOMAIN=your-tenant.us.auth0.com
AUTH0_AUDIENCE=my-api
AUTH0_CLIENT_ID=abc123
APP_NAME=SyntaxSentinels
```

---

## Running the Server

1. Ensure the virtual environment is **activated**.
2. **Start** the server:
   ```bash
   python app.py
   ```
   or, if you’re using the Flask CLI:
   ```bash
   flask run
   ```
3. By default, visit [http://localhost:5000/](http://localhost:5000/) (or whichever port you set) to access the app.

---

**That’s it!** Your Flask backend for SyntaxSentinels should now be up and running. Adjust the commands or details above as needed for your specific setup.
