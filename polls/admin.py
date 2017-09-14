from django.contrib import admin
from .models import Choice, Category, Question, Profile, State

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Choice)
admin.site.register(Profile)
admin.site.register(State)