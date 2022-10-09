from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json', views.json, name='json'),
    path('json/authors', views.json_authors, name='json_authors'),
    path('json/random', views.json, name='json'),
    path('stats', views.stats, name='stats'),
    path('random', views.index, name='index'),
    path('add', views.add, name='add'),

    path('authors', views.authors, name='authors'),
    path('authors/<str:author_name>', views.authors, name='authors'),
    re_path(r'^humans\.txt$', TemplateView.as_view(template_name="humans.txt", content_type='text/plain')),
]