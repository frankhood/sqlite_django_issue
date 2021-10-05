from django.contrib import admin
from django.db import models

from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ("choice_text", "votes",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date",)
    inlines = [ChoiceInline]
    fieldsets = (
        (None, {"fields": (
            ("question_text", "pub_date"),
        )}),
    )