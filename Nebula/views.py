import os
import time
from django.views.generic import TemplateView

from movies.models import Recommendation, Category, Review


class HomeView(TemplateView):
    template_name = 'Nebula/home.html'

    def get_context_data(self, **kwargs):
        time.sleep(10)

        context = super().get_context_data(**kwargs)

        context['recommendations'] = Recommendation.objects.all()
        context['categories'] = Category.objects.all()
        context['reviews'] = Review.objects.order_by('-added')[:4]
        context['test'] = os.environ.get('TEST')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
