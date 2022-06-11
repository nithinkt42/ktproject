from django.urls import path
from . import views
urlpatterns= [
    path ('',views.nithin),
    path ('html',views.htmlpage)

]