from django.contrib import admin
from .models import Category, Habit, DailyLog, Reminder

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'goal_frequency', 'current_streak']
    list_filter = ['category']

@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ['habit', 'date', 'completed']
    list_filter = ['habit', 'date', 'completed']

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['habit', 'time']