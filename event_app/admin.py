from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Event, Booking
from django.forms import ModelForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_mobile', 'get_dob')

    def get_mobile(self, obj):
        return obj.userprofile.mobile
    def get_dob(self, obj):
        return obj.userprofile.dob

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Event)


from django.contrib import admin
from .models import Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

admin.site.register(Booking, BookingAdmin)
