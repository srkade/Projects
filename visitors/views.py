from django.shortcuts import render
import csv
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Visitor
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Visitor.objects.create(name=name, email=email, phone=phone)
        return redirect('thank_you')
    return render(request, 'visitors/index.html')

def thank_you(request):
    return render(request, 'visitors/thank_you.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_panel')
        else:
            error = "Invalid username or password"
            return render(request, 'visitors/admin_login.html', {'error': error})
    return render(request, 'visitors/admin_login.html')

@login_required
def admin_panel(request):
    search_query = request.GET.get('search', '')
    visitors = Visitor.objects.filter(
        name__icontains=search_query
    ).order_by('-visit_time')
    return render(request, 'visitors/admin_panel.html', {'visitors': visitors, 'search_query': search_query})

@login_required
def visitor_checkout(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    visitor.checkout_time = timezone.now()
    visitor.save()
    return redirect('admin_panel')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def export_visitors_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="visitors.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Visit Time', 'Checkout Time'])

    visitors = Visitor.objects.all().values_list('name', 'email', 'phone', 'visit_time', 'checkout_time')
    for visitor in visitors:
        writer.writerow(visitor)

    return response
