from django.conf.urls import patterns, url
from django_prometheus import exports

urlpatterns = [
    url(r'^metrics$', exports.ExportToDjangoView,
        name='prometheus-django-metrics'),
]
