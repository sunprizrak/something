from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactsForm


class ChoiceLanguageView(TemplateView):
    template_name = 'main/choice_lang.html'
    extra_context = {
        'title': 'ChoiceLanguage'
    }


class HomeView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Home'
    }


class ContactsView(FormView):
    form_class = ContactsForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('contacts')
    extra_context = {
        'title': 'Contacts'
    }

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Форма отправлена успешно!')
        return super(ContactsView, self).form_valid(form)
