from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Habit, Category, DailyLog

def habit_list(request):
    habits = Habit.objects.select_related('category').all()
    

    for habit in habits:
        days_this_month = 30 
        completed_days = DailyLog.objects.filter(
            habit=habit, 
            completed=True,
            date__month=timezone.now().month
        ).count()
        habit.rate = int((completed_days / days_this_month) * 100) if days_this_month > 0 else 0
    
    return render(request, 'habits/habit_list.html', {
        'habits': habits
    })

def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habits/habit_detail.html', {'habit': habit})

def habit_progress(request):
    habits = Habit.objects.select_related('category').all()
    progress_data = []
    
    for habit in habits:
        completed_logs = DailyLog.objects.filter(
            habit=habit, 
            completed=True
        ).count()
        total_logs = DailyLog.objects.filter(habit=habit).count()
        rate = (completed_logs / total_logs * 100) if total_logs > 0 else 0
        
        progress_data.append({
            'name': habit.name,
            'category': habit.category.name,
            'rate': round(rate, 1),
            'streak': habit.current_streak
        })
    
    return render(request, 'habits/habit_progress.html', {
        'progress_data': progress_data
    })

def category_habits(request, pk): 
    category = get_object_or_404(Category, pk=pk)
    habits = Habit.objects.filter(category=category)
    return render(request, 'habits/category_habits.html', {'category': category, 'habits': habits})