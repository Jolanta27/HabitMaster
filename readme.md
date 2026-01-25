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
![Lista nawyków](https://github.com/user-attachments/assets/9c5694a9-25ef-4fda-8a72-a9c73ad0c7e1)
![Zrzut ekranu 2026-01-25 o 13 54 06](https://github.com/user-attachments/assets/84a731c4-4fe7-4fc0-aa77-4f1fffc008d9)
![Zrzut ekranu 2026-01-25 o 13 54 54](https://github.com/user-attachments/assets/6de1daf5-8b51-459a-b6e4-67c7e371e41c)
![Zrzut ekranu 2026-01-25 o 14 00 25](https://github.com/user-attachments/assets/9470ed77-fc8d-43fb-b564-3445a3ddbbbe)
![Zrzut ekranu 2026-01-25 o 14 06 37](https://github.com/user-attachments/assets/20d8fa22-3ca3-4418-a76d-2a9810489d29)

## 📱 Demo (lokalnie) po instalacji:
🌐 Lista: http://127.0.0.1:8000/
📊 Progress: http://127.0.0.1:8000/progress/
⚙️ Admin: http://127.0.0.1:8000/admin/

## 🛠️ Instalacja:
```bash
git clone https://github.com/Jolanta27/HabitMaster
cd HabitMaster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate lub python manage.py migrate
python3 manage.py createsuperuser lub python manage.py createsuperuser
python3 manage.py runserver lub python3 manage.py runserver

Django 5.2 | Python 3.14 | SQLite3 | HTML5/CSS3 | Git/GitHub

