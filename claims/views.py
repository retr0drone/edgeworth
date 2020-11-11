from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . models import Claims
from . forms import ClaimsCreateForm


class ClaimsListView(generic.ListView):
    template_name = 'claims/claims_list.html'
    queryset = Claims.objects.all()


class ClaimsDetailView(generic.DetailView):
    model = Claims
    template_name = 'claims/claims_detail.html'
    #     # if not detail.user == self.request.user:
    #     #     raise Http404
    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])


class ClaimsCreateView(generic.CreateView):
    template_name = 'claims/claims_create.html'
    form_class = ClaimsCreateForm

    def get_success_url(self):
        return reverse('claims')

    def form_valid(self, form):
        form.save()
        return super(ClaimsCreateView, self).form_valid(form)


class ClaimsUpdateView(generic.UpdateView):
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


class ClaimsDeleteView(generic.DeleteView):
    template_name = 'claims/claims_delete.html'
    queryset = Claims.objects.all()

    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('claims')







