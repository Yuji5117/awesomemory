from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     self.object = user
    #     return HttpResponseRedirect(self.get_success_url())


    # Login automatically after signup #
    # def form_valid(self, form):
    #     super().form_valid(form)
    #     login(self.request, self.form)
    #     return valid