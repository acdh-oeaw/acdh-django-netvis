from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from example.models import MyText

class IndexView(TemplateView):

    template_name = 'example/index.html'


class MyTextDetailViewSimple(DetailView):

    model = MyText
    template_name = 'example/mytext_simple.html'


class MyTextDetailView(DetailView):

    model = MyText
    template_name = 'example/mytext.html'
