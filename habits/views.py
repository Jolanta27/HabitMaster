from django.shortcuts import render, get_object_or_404
from .models import Habit, Category, DailyLog

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})

def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habits/habit_detail.html', {'habit': habit})

def habit_progress(request):  
    habits = Habit.objects.all()
    progress_data = []
    for habit in habits:
        logs = DailyLog.objects.filter(habit=habit)[:30]
        rate = (logs.filter(completed=True).count() / 30 * 100) if logs else 0
        progress_data.append({'habit': habit, 'rate': round(rate, 1)})
    return render(request, 'habits/habit_progress.html', {'progress_data': progress_data})

def category_habits(request, pk): 
    category = get_object_or_404(Category, pk=pk)
    habits = Habit.objects.filter(category=category)
    return render(request, 'habits/category_habits.html', {'category': category, 'habits': habits})