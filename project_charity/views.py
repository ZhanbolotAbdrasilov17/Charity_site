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
    slider_1 = Slider.objects.get(pk=1)
    slider_2 = Slider.objects.get(pk=2)
    slider_3 = Slider.objects.get(pk=3)

    desc_1 = Desc.objects.get(pk=1)
    desc_2 = Desc.objects.get(pk=2)


    about = About_us_mainpaig.objects.all()
    partners = Partner.objects.all()

    context = {"about": about, "partners": partners, "slider_1":slider_1,
               "slider_2": slider_2, "slider_3": slider_3,
               "desc_1": desc_1, "desc_2": desc_2,}
    return render(request, 'home.html', context)

def about(request):
    about = About_page_text.objects.all()
    context = {"about": about,}
    return render(request, 'about.html', context)


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
    images1 = Gallery_1.objects.all()
    images2 = Gallery_2.objects.all()
    images3 = Gallery_3.objects.all()
    images4 = Gallery_4.objects.all()
    images5 = Gallery_5.objects.all()
    images6 = Gallery_6.objects.all()
    images7 = Gallery_7.objects.all()
    images8 = Gallery_8.objects.all()
    images9 = Gallery_9.objects.all()
    images10 = Gallery_10.objects.all()
    images11 = Gallery_11.objects.all()
    images12 = Gallery_12.objects.all()

    context = {
        'images1': images1, 'images2': images2, 'images3': images3, 'images4': images4,
        'images5': images5, 'images6': images6, 'images7': images7, 'images8': images8,
        'images9': images9, 'images10': images10, 'images11': images11, 'images12': images12,
    }
    return render(request, 'gallery.html', context)



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
                'charity_kyrgystan@mail.ru',
                ['itpythonzhanbolot@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('home'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')