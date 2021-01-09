from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . models import Claims, Comments
from . forms import ClaimsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum

# Django Rest Framework
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from . serializers import ClaimsSerializer


# Django Rest Framework Serializers Start

class ClaimsRestListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClaimsSerializer
    queryset = Claims.objects.all()

# Django Rest Framework Serializers End


def home(request):
    return render(request, 'index.html')
    

class ClaimsListView(LoginRequiredMixin, generic.ListView):
    model = Claims
    queryset = Claims.objects.all()
    template_name = 'claims/claims_list.html'
    context_object_name = 'claims_list'
    paginate = 10

    def get_queryset(self):
        return Claims.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ClaimsListView, self).get_context_data(**kwargs)
        context['claims_count'] = self.get_queryset().count()
        context['claims_under_review'] = self.queryset.filter(user=self.request.user, status='Under Review').count()
        context['claims_in_progress'] = self.queryset.filter(user=self.request.user, status='In Progress').count()
        context['claims_completed'] = self.queryset.filter(user=self.request.user, status='Completed').count()
        context['total_debt_amount'] = Claims.objects.filter(pk=self.kwargs.get('pk')).aggregate(total_debt_amount=Sum('debt_amount'))
        return context




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







