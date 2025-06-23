from django.db import models

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('anxious', 'Anxious'),
        ('excited', 'Excited'),
        ('neutral', 'Neutral'),
    ]

    title = models.CharField(max_length=100, blank=True, help_text="Optional title for your entry")
    date = models.DateField(auto_now_add=True, help_text="Date of the mood entry")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the entry was created")
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, help_text="Select your mood")
    notes = models.TextField(blank=True, null=True, help_text="Additional notes about your mood")

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Mood Entry"
        verbose_name_plural = "Mood Entries"

    def __str__(self):
        title_part = f" | {self.title}" if self.title else ""
        return f"{self.date}{title_part} - {self.get_mood_display()}"
