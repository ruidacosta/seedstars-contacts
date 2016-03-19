from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list', views.list, name='List'),
    url(r'^add$', views.add, name='Add'),
    url(r'^insert', views.insert, name='Insert'),
    url(r'^$', views.index, name='Welcome'),
]