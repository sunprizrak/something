from django.urls import path
from .views import ChoiceLanguageView, HomeView, ContactsView

urlpatterns = [
    path('', ChoiceLanguageView.as_view(), name='choice_lang'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]