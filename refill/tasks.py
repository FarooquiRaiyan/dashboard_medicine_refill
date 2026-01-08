from celery import shared_task
from .models import MedicineDetails, Notification

@shared_task
def send_inapp_reminders():
    REMINDER_DAYS = [3, 1]

    medicines = MedicineDetails.objects.all()

    for med in medicines:
        days_left = med.days_left()

        if days_left in REMINDER_DAYS:
            Notification.objects.get_or_create(
                user=med.user,
                message=f"Your medicine '{med.med_name}' has only {days_left} day(s) left."
            )
