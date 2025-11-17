from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    appr_minutes_todo = models.IntegerField(default=15)
    importance = models.PositiveIntegerField(default=1)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    notify_before_min = models.IntegerField(default=15)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title