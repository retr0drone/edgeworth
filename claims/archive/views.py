from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . models import Claims, Comments
from . forms import ClaimsCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum

#Django Rest Framework
from rest_framework.views import APIView #for class based views
from rest_framework.decorators import api_view #for function based views
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from . serializers import ClaimsSerializer, OwnerSerializer, CommentSerializer
from . permissions import IsOwnerPermission
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets #for routers. includes generic CRUD. shit!!!

User = get_user_model()

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
        # context['total_debt_amount'] = Claims.objects.filter(pk=self.kwargs.get('pk')).aggregate(total_debt_amount=Sum('claims_list__debt_amount'))
        return context


# Django Rest Framework Serializers Start
# CRUD Start
class ClaimsRestListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = Claims.objects.all()
        serializer = ClaimsSerializer(queryset, many=True)
        # if serializer.is_valid():
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ClaimsSerializer(data=request.data) # for api's not request.POST in Django
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        claim = Claims.objects.get(pk=pk)
        serializer = ClaimsSerializer(claim, data=request.data) # for api's not request.POST in Django
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        claim = Claims.objects.get(pk=pk)
        claim.delete()
        return Response(status=HTTP_204_NO_CONTENT)



@csrf_exempt
def claims_rest_list_view(request):
    if request.method == 'GET':
        queryset = Claims.objects.all()
        serializer = ClaimsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = ClaimsSerializer(data=data)
        if selializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def claims_rest_detail_view(request, pk):
    try:
        claims = Claims.objects.get(pk=pk)
    except Claims.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        selializer = ClaimsSerializer(claims)
        return JsonResponse(serlializer.data)
    # updating specific instance
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = ClaimsSerializer(claims, data=data)
        if serlializer.is_valid():
            serializer.save()
            return JsonResponse(serlializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        claims.delete()
        return HttpResponse(status=204)
# CRUD End

# Mixins Start

class ClaimsRestMixinListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

# Mixins End

# Generic Class Based Views Start

class ClaimsRestApiListView(generics.ListAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAuthenticated,)

class ClaimsRestApiDetailView(generics.RetrieveAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission)

class ClaimsRestApiDeleteView(generics.DestroyAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer


class OwnerApiDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = OwnerSerializer

class CommentApiDetailView(generics.RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

# Generic Class Based Views End

# Routers Start

class ClaimsViewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAuthenticated,)

# Routers End

# Django Rest Framework Serializers End


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







