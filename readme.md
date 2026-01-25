# 🎯 Habit Tracker - Django Web App
**SWPS Projektowanie WWW - Zaliczenie**

[![Django](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)

## ✨ Funkcjonalności:
- ✅ **Modele Django** (Category, Habit, DailyLog, Reminder)
- ✅ **Lista nawyków** z animowanymi paskami progresu
- ✅ **Detail view z CRUD** (`/1/` - edycja + usuwanie nawyku)
- ✅ **Widok statystyk** `/progress/` z responsywnymi kartami
- ✅ **Responsywny design** (mobile-first, gradienty CSS)

## 📸 Demo Screenshots
<div align="center">
![Zrzut ekranu 2026-01-25 o 13 51 23](https://github.com/user-attachments/assets/9c5694a9-25ef-4fda-8a72-a9c73ad0c7e1)


</div>

## 📱 Demo (lokalnie):
🌐 Lista: http://127.0.0.1:8000/
📊 Progress: http://127.0.0.1:8000/progress/
⚙️ Admin: http://127.0.0.1:8000/admin/

undefined

## 🛠️ Instalacja:
```bash
git clone https://github.com/Jolanta27/HabitMaster
cd HabitMaster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Django 5.2 | Python 3.14 | SQLite3 | HTML5/CSS3 | Git/GitHub

