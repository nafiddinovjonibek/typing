from django.db import models


class Text(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Oson'),
        ('medium', "O'rta"),
        ('hard', 'Qiyin'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def word_count(self):
        return len(self.content.split())


class TypingResult(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='results')
    wpm = models.FloatField()
    accuracy = models.FloatField()
    time_taken = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text.title} - {self.wpm} WPM"
