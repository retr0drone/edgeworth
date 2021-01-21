from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.shortcuts import render
from django.views import generic
from claims.models import Claims
from . mixins import StaffUserMixin
from . forms import ClaimsCreateForm

# CLAIMS

class ClaimsListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/claims_list.html'
    queryset = Claims.objects.all().order_by('-date_created')
    paginate_by = 20
    context_object_name = 'claims'

    

    def get_context_data(self, **kwargs):
        context = super(ClaimsListView, self).get_context_data(**kwargs)
        context['claims_count'] = self.get_queryset().count()
        context['claims_under_review'] = self.queryset.filter(status='Under Review').count()
        context['claims_in_progress'] = self.queryset.filter(status='In Progress').count()
        context['claims_completed'] = self.queryset.filter(status='Completed').count()
        return context


class ClaimsDetailView(LoginRequiredMixin, StaffUserMixin, generic.DetailView):
    model = Claims
    template_name = 'staff/claims_detail.html'
    
   
class ClaimsCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name = 'staff/claims_create.html'
    form_class = ClaimsCreateForm

    def get_success_url(self):
        return reverse('staff:client-claims')

    def form_valid(self, form):
        claim = form.save(commit=False)
        claim.user = self.request.user
        claim.save()
        return super(ClaimsCreateView, self).form_valid(form)


class ClaimsUpdateView(LoginRequiredMixin, StaffUserMixin, generic.UpdateView):
    template_name = 'staff/claims_update.html'
    form_class = ClaimsCreateForm
    queryset = Claims.objects.all()

    def get_success_url(self):
        return reverse("staff:client-claims")

    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.save()
        return super(ClaimsUpdateView, self).form_valid(form)


class ClaimsDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name = 'staff/claims_delete.html'
    queryset = Claims.objects.all()

    def get_object(self):
        return get_object_or_404(Claims, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('claims')


# CLIENT PROFILE


# class ClientDetailView(LoginRequiredMixin, StaffUserMixin, generic.DetailView):
class ClientDetailView(LoginRequiredMixin, StaffUserMixin, generic.TemplateView):
    template_name = 'staff/client_detail.html'
