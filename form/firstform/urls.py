from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^requirement',views.require,name='require'),
    url(r'^newenq',views.require,name='requirement'),
    url(r'^database',views.database,name='database'),
    ]
