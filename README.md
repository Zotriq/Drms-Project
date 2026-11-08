# Disaster Relief Management System: Backend API

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

REST API for a **Disaster Relief Resource Management System (DRMS)**. It coordinates NGOs, volunteers and victims
during emergencies such as floods and earthquakes, tracking relief resources, SOS requests, shelters and tasks
in one place.

## Modules

| Area | What it covers |
|---|---|
| **SOS requests** | Victims report emergencies with location and urgency, and track the status of their request |
| **Resources** | Food, water, medicine and shelter stock, with status tracking |
| **Volunteers & tasks** | Volunteer registration, task assignment and progress updates |
| **NGOs & shelters** | Organization records and shelter capacity |
| **Priority zones** | Marking the hardest-hit areas so aid goes there first |
| **Notifications & reports** | Alerts, distribution reports and feedback |
| **Users & admin** | Accounts, roles and an audit log of actions |

## Architecture

A layered Flask application:

```
src/
  api/            Flask blueprints (one per module)
  controllers/    Request handling
  services/       Business logic
  repositories/   Database queries
  models/         Data models
  db/             MySQL connection
  config.py       Settings loaded from .env
  main.py         App entry point
```

## Getting started

```bash
cd src
pip install -r requirements.txt
```

Copy `src/.env.example` to `src/.env` and fill in your values:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=drms
```

Run:

```bash
python main.py
```

*Built as a university Software Engineering project.*
