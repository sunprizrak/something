from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactsForm
from django.contrib.gis.geoip2 import GeoIP2


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ChoiceLanguageView(TemplateView):
    template_name = 'main/choice_lang.html'
    extra_context = {
        'title': 'ChoiceLanguage'
    }

    def get(self, request, *args, **kwargs):
        # ip = get_client_ip(request=request)
        ip = '37.214.28.13'  # '37.214.28.13'
        g = GeoIP2()
        user_country = g.country_name(ip)

        print(g.country_name(ip))

        if user_country in ['Belarus', 'Russia']:
            self.extra_context['choose_language'] = 'Выберите язык'
        elif user_country in ['Montenegro', 'Serbia']:
            self.extra_context['choose_language'] = 'Izaberi jezik'
        else:
            self.extra_context['choose_language'] = 'Choose language'

        return super(ChoiceLanguageView, self).get(request, *args, **kwargs)


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
