from django.urls import path
from . import views
from .views import CombinedView, SuccessView

urlpatterns = [
    path('', CombinedView.as_view(), name='index'),
    path('contact/', CombinedView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('feedback/', CombinedView.as_view(), name='feedback'),
]
