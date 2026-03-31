from django.contrib import admin
from .models import Text, TypingResult


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'word_count', 'created_at')
    list_filter = ('difficulty',)


@admin.register(TypingResult)
class TypingResultAdmin(admin.ModelAdmin):
    list_display = ('text', 'wpm', 'accuracy', 'time_taken', 'created_at')
