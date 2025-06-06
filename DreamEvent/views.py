from django.shortcuts import render
def index(request):
    return render(request,'index.html')

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