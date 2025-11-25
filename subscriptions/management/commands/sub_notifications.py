import datetime
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.core.management import BaseCommand
from subscriptions.models import Subs
from prcalendar.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = timezone.now().date()
        for sub in Subs.objects.filter(payment_date__lte=today):
            while sub.payment_date <= today:
                match sub.cycle:
                    case "Daily": sub.payment_date += datetime.timedelta(days=1)
                    case "Monthly": sub.payment_date += relativedelta(months=1)
                    case "Weekly": sub.payment_date += datetime.timedelta(weeks=1)
                    case "Fortnight": sub.payment_date += datetime.timedelta(weeks=2)
            sub.save()

        subs = Subs.objects.filter(payment_date=(today + datetime.timedelta(days=1)))
        for sub in subs:
            if sub.cycle == "Daily":
                continue
            message = f'''
                        Вітаю! Наступного дня ваші кошти будуть зняти на цю підписку:
                        Дата: {sub.payment_date}
                        Ціна: {sub.cost}
                      '''
            try:
                send_mail(
                    f"Підписка: {sub.name}",
                    message,
                    EMAIL_HOST_USER,
                    [sub.owner.email],
                )
            except Exception as e:
                print(f"Error: {e}; id: {sub.pk}")