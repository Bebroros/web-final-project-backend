import datetime
from django.core.mail import send_mail
from django.utils import timezone
from django.core.management import BaseCommand
from events.models import Event
from prcalendar.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = timezone.now()
        notification_time = now + datetime.timedelta(hours=1)
        window_time = notification_time + datetime.timedelta(minutes=5)

        events = Event.objects.select_related('owner').filter(
            start_at__gte=notification_time,
            start_at__lte=window_time,
            notified=False,
        )

        for event in events:
            message = f'''Всього лиш за годину відбудеться запланована подія!
                         Опис події: {event.description}
                         Початок: {event.start_at}
                         Закінчення: {event.end_at} 
                      '''
            try:
                send_mail(
                    f"Подія: {event.title}",
                    message,
                    EMAIL_HOST_USER,
                    [event.owner.email],
                )
                event.notified = True
                event.save()
            except Exception as e:
                print(f"Error: {e}; id: {event.pk}")
