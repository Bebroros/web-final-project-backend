from django.db import models
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    importance = models.PositiveIntegerField(default=1)
    start_at = models.DateTimeField(db_index=True)
    end_at = models.DateTimeField()
    notified = models.BooleanField(default=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
