from django.db import models
from django.conf import settings

class Subs(models.Model):
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    FORTNIGHT = "fortnight"

    CYCLE_CHOICES= {
        MONTHLY: "Monthly",
        WEEKLY: "Weekly",
        DAILY: "Daily",
        FORTNIGHT: "Fortnight",
    }

    name = models.CharField(max_length=32)
    payment_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cycle = models.CharField(max_length=10,
                             choices=CYCLE_CHOICES,
                             default=MONTHLY)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name