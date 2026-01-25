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
 ![](https://github.com/user-attachments/assets/230daee3-07ae-4a18-b6c0-1b9b92c91b0d)
 ![](https://github.com/user-attachments/assets/7742996a-39b9-49af-89d4-38ef577f67ab)
 ![](https://github.com/user-attachments/assets/523f3f75-d6ed-4326-87e4-81ba334924c0)
 ![](https://github.com/user-attachments/assets/81b613f0-d228-4afa-bf54-17202cc9609c) 
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

