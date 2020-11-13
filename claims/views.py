from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . models import Claims
from . forms import ClaimsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ClaimsListView(LoginRequiredMixin, generic.ListView):
    model = Claims
    template_name = 'claims/claims_list.html'
    context_object = 'claims_list'
    paginate = 10
    queryset = Claims.objects.all()

    def get_queryset(self):
        return Claims.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ClaimsListView, self).get_context_data(**kwargs)
        context['claims_count'] = self.get_queryset().count()
        context['claims_under_review'] = self.queryset.filter(user=self.request.user, status='Under Review').count()
        context['claims_in_progress'] = self.queryset.filter(user=self.request.user, status='In Progress').count()
        context['claims_completed'] = self.queryset.filter(user=self.request.user, status='Completed').count()
        

class ClaimsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Claims
    template_name = 'claims/claims_detail.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Claims.objects.filter(user=self.request.user)
        else:
            return Claims.objects.none()
        return redirect('claims:claims')


class ClaimsCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'claims/claims_create.html'
    form_class = ClaimsCreateForm

    def get_success_url(self):
        return reverse('claims:claims')

    def form_valid(self, form):
        claim = form.save(commit=False)
        claim.user = self.request.user
        claim.save()
        return super(ClaimsCreateView, self).form_valid(form)


class ClaimsUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'claims/claims_update.html'
    form_class = ClaimsCreateForm
    queryset = Claims.objects.all()

    def get_success_url(self):
        return reverse("claims:claims")

    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.save()
        return super(ClaimsUpdateView, self).form_valid(form)


class ClaimsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'claims/claims_delete.html'
    queryset = Claims.objects.all()

    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('claims')







