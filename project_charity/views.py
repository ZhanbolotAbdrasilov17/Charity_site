from django.shortcuts import render
from django.conf import settings
from django.views.generic import DetailView

from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import MailForm
from django.views import View


def home(request):
    about = About_us_mainpaig.objects.all()
    context = {"about": about,}
    return render(request, 'home.html', context )

def about(request):
    return render(request, 'about.html', )


def causes(request):
    cases = HelpCase.objects.all()
    context = {'cases': cases}

    return render(request, 'causes.html', context)

class CaseDetail(DetailView):
    model = HelpCase
    template_name = "case_details.html"
    context_object_name = 'case'
    pk_url_kwarg = 'case_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def causes_single(request):
    return render(request, 'causes_single.html', )

def gallery(request):
    return render(request, 'gallery.html', )


def contact(request):
    return render(request, 'contact.html', )



class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            last_sender = Email.objects.last()
            message = f'Почта: {last_sender.address}\n'

            send_mail(
                'Почта клиента или партнера',
                message,
                'oriyental.treyd@mail.ru',
                ['orienttrade2016@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('home'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')