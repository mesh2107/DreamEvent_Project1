from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)  # 👈 Differentiates roles
    mobile = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  # ✅ Add this

    def __str__(self):
        return self.name

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Booking(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Guest")
    email = models.EmailField(default="guest@example.com")
    mobile = models.CharField(max_length=15, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    guests = models.PositiveIntegerField(default=1)
    payment_method = models.CharField(max_length=50, blank=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        today = timezone.now().date()

        if self.booking_date:
            if self.booking_date < today:
                raise ValidationError({'booking_date': 'Booking date cannot be in the past.'})

        if self.booking_date and self.end_date:
            if self.end_date < self.booking_date:
                raise ValidationError({'end_date': 'End date cannot be before booking date.'})

    def __str__(self):
        return f"{self.name} - {self.event.name}"
