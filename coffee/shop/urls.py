from django.conf.urls import url
from . import views
from shop.views import IndexView


app_name = 'shop'

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register/', views.RegisterCreate.as_view(), name='register'),
	url(r'^coffee/', views.coffee_view, name='coffee_view'),
	url(r'^baked/', views.baked_view, name='baked'),
	url(r'^contacts/', views.contacts_view, name='contacts'),

]
