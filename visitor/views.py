from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,DeleteView,TemplateView,FormView
from visitor.models import Visitor

# Create your views here.

class VisitorHomeView(TemplateView):
    template_name = 'visitor/visitor.html'

class VisitorListView(ListView):
    model = Visitor
    # 디폴트로 모른 데이터를 가져옴
    context_object_name = "visitor_list"

class VisitorDetailView(DetailView):
    model = Visitor

class VisitorCreateView(CreateView):
    model = Visitor
    template_name = 'visitor/visitor_create.html'
    fields = '__all__'
    success_url = reverse_lazy('visitor:visitor_list')

class VisitorDeleteView(DeleteView):
    model = Visitor
    success_url = reverse_lazy('visitor:visitor_list')
