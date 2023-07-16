from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('gallery', gallery, name='gallery'),
    path('causes', causes, name='causes'),
    path('causes/<int:case_id>/', CaseDetail.as_view(), name='case_details'),
    path('about', about, name='about'),
    path('mail/create/', MailCreateView.as_view(), name='mail_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)