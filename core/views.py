from django.shortcuts import render, redirect
from core.models import *
from core.forms import ContactForm
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            form.save()
            # Send email notification
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            send_mail(
                'New Contact Form Submission',
                f'You have a new contact form submission from {name} {surname}, email: {email}.\n\n http://127.0.0.1:8000/admin/core/contact/{data.id}/change/',
                'murad.aghazada@div.edu.az',
                ['murad.aghazada@div.edu.az'],
                fail_silently=False,
            )
            send_mail(
                'Tedspace Contact Form Submission Successful!',
                f'Dear {name},\n\nThank you for reaching out to Tedspace. We have received your message and will get back to you shortly.\n\nBest regards,\nTedspace Team',
                'murad.aghazada@div.edu.az',
                [email],
                fail_silently=False,
            )

            return redirect('/')
    form = ContactForm()
    blog = Blog.objects.order_by("-id")
    partners = Partner.objects.order_by("-id")
    context = {
        'blog': blog,
        'partners': partners,
        'form':form
    }
    return render(request, 'index.html', context)