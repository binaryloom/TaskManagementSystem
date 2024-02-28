from django.shortcuts import render

from abstract.views import TemplateView

# Create your views here.


class DashboardView(TemplateView):
    template_name = "task_management/dashboard.html"
