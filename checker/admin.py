from django.contrib import admin
from .models import PlagiarismResult

@admin.register(PlagiarismResult)
class PlagiarismResultAdmin(admin.ModelAdmin):
    list_display = ("id", "similarity", "checked_at")
    ordering = ("-checked_at",)
