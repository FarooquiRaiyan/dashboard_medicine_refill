from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class MedicineDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    med_name = models.CharField(max_length=200)
    med_user = models.CharField(max_length=100, default="Self")
    start_date = models.DateField()
    per_day_tabs =models.PositiveIntegerField(default=0)
    total_tablet_count = models.PositiveIntegerField(default=0)
    total_tabs_packet = models.PositiveIntegerField(default=0)
    
    
    
    
    def total_days(self):
        if self.per_day_tabs == 0:
            return 0
        total_tablets = self.total_tablet_count * self. total_tabs_packet
        return total_tablets//self.per_day_tabs
    
    
    def days_left(self):
        today = now().date()
        days_used = (today - self.start_date).days
        remaining = self.total_days() - days_used
        return max(remaining, 0)
    
    def __str__(self):
        return self.med_name
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)