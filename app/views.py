from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from classicelectricals import settings
# Create your views here.
def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def requestq(request):
    return render(request, 'request.html')

def contact_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        subject = request.POST.get("subject", "No Subject")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Subject: {subject}
        Message: {message}
        """

        email_message = EmailMessage(
            subject=f"New Contact Request: {subject}",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.COMPANY_EMAIL], 
            reply_to=[email],
        )

        try:
            email_message.send()
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

        return redirect("contact")

    return render(request, "contact.html")

def request_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        subject = request.POST.get("subject", "No Subject")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Subject: {subject}
        Message: {message}
        """

        email_message = EmailMessage(
            subject=f"New Contact Request: {subject}",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.COMPANY_EMAIL], 
            reply_to=[email],
        )

        try:
            email_message.send()
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

        return redirect("requestq")

    return render(request, "request.html")