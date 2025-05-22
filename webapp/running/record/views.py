from django.shortcuts import render # May not be strictly needed if only using CBVs
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RecordActivity
from .forms import RecordActivityForm

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = RecordActivity
    form_class = RecordActivityForm
    template_name = 'record/record_form.html' # Will create this template later
    success_url = reverse_lazy('record_list') # Will define this URL name later

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class RecordListView(LoginRequiredMixin, ListView):
    model = RecordActivity
    template_name = 'record/record_list.html' # Will create this template later
    context_object_name = 'records'

    def get_queryset(self):
        # Filter records for the currently logged-in user, order by most recent
        return RecordActivity.objects.filter(username=self.request.user).order_by('-date')
