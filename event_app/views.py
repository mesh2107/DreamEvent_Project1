from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Event, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Booking
from decimal import Decimal
import razorpay

# pages
def home(request):
    events = Event.objects.all()
    return render(request, 'index.html',{'events': events})
def about(request):
    return render(request,'about.html')
def event(request):
    return render(request,'Event.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
def privateparty(request):
    return render(request,'privateparty.html')
def wedding(request):
    return render(request,'wedding.html')
def when(request):
    return render(request,'when-where.html')
def blog(request):
    return render(request,'blog.html')
def booking(request):
    return render(request,'booking.html')

# user registration

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        address = request.POST['address']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1, email=email,
                                        first_name=first_name, last_name=last_name)
        
        # Create profile only if it doesn't exist
        if not UserProfile.objects.filter(user=user).exists():
            UserProfile.objects.create(
                user=user,
                mobile=mobile,
                dob=dob,
                address=address,
                is_admin=False  # Or True depending on role
            )

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

# user login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')
# logout user
def logout_user(request):
    logout(request)
    return redirect('login')



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'event_detail.html', {'event': event})



@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    advance_payment = round(Decimal(event.price) * Decimal('0.4'), 2)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Booking.objects.create(
                event=event,
                user=request.user,
                name=cd['name'],
                email=cd['email'],
                mobile=cd['mobile'],
                booking_date=cd['booking_date'],
                end_date=cd['end_date'],
                guests=cd['guests'],
                payment_method=cd['payment_method'],
                transaction_id=cd['transaction_id'],
                advance_amount=advance_payment
            )
            messages.success(request, 'Booking successful!')
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {
        'event': event,
        'form': form,
        'advance_payment': advance_payment
    })
    
    
    # users bookingggg data

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    return render(request, 'my_bookings.html', {'bookings': bookings})
# user-admin

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

@login_required
def admin_dashboard(request):
    if not request.user.userprofile.is_admin:
        return redirect('user_dashboard')
    events = Event.objects.all()
    return render(request, 'admin_dashboard.html', {'events': events})

