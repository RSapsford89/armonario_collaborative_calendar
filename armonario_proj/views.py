from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    return render(request, 'base.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_subject = f'Contact from {name}'
            email_content = f'{name}, {email} from Armonario sent this message:\n {message} '
            send_mail(
                email_subject,
                email_content,
                email,
                [email],
                fail_silently=False,
            )
            # show a success message as example - this info appears in the
            #  Terminal instead of directing to a real address
            messages.success(request, f'Thank you for contacting us! We sent a copy to {email}.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
