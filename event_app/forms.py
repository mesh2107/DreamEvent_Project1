from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        self.instance.booking_date = cleaned_data.get('booking_date')
        self.instance.end_date = cleaned_data.get('end_date')
        self.instance.clean()  # Call model-level validation
        return cleaned_data
