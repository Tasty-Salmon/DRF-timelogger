# Time Logger App

A simple web-based retrospective time logger application built with **Django Rest Framework (DRF)** and **Django Templates**.  
Designed to practice API-first development while keeping the app user-friendly with basic HTML rendering.

---

## 📚 Features

- **Log** daily activities with start and end times.
- **List** activities grouped by day.
- **View** activities for a specific date.
- **Create** and **edit** log entries easily.
- **API-first** structure (DRF ListCreateAPIView, RetrieveUpdateDestroyAPIView).
- **Basic TailwindCSS UI** for a clean and modern look.

---

## 🚀 Tech Stack

- **Backend**: Django 5, Django Rest Framework
- **Frontend**: Django Templates + TailwindCSS
- **Database**: SQLite (default Django DB)

---

## 🛠️ Project Structure

| File | Purpose |
|-----|---------|
| `views.py` | DRF generic views (ListCreateAPIView, RetrieveUpdateDestroyAPIView) + Django Create/Update Views |
| `models.py` | `EveningLog` model for storing activity logs |
| `serializers.py` | Serializers for EveningLog and User models |
| `forms.py` | Django Form for log creation/editing |
| `templates/` | TailwindCSS-styled HTML templates |
| `urls.py` | URL routing for views |

---

## 📄 Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | List all logs, grouped by day (HTML or JSON) |
| `POST` | `/` | Create a new log entry (API) |
| `GET` | `/day-view?date=YYYY-MM-DD` | View logs for a specific date (HTML) |
| `GET/POST` | `/create/` | Form page to create a new log (HTML) |
| `GET/POST` | `/edit/<id>/` | Form page to edit an existing log (HTML) |
| `GET` | `/users/` | List all users (API) |
| `GET/PUT/DELETE` | `/users/<id>/` | Retrieve, update, or delete a user (API) |

---

## 🧪 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/time-logger.git
   cd time-logger
