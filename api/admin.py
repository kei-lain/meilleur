from django.contrib import admin
from .models import Goal, Category, Solution, Journal, Task
# Register your models here.
admin.site.register(Goal)
admin.site.register(Category)
admin.site.register(Solution)
admin.site.register(Journal)
admin.site.register(Task)