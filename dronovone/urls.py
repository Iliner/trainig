from django.conf.urls import url 
from . import views

# urlpatterns = [
#     url(r"^$", views.index, name="index"),
#     url(r"^good/$", views.good, name='good'),
# ]


# urlpatterns = [
#     url(r"^(?:\?id=(?P<id>\d+))?$", views.index, name="index"),
#     url(r"^good/\?id=(?P<id>\d+)$", views.good, name='good'),
# ]


urlpatterns = [
    url(r"^(?:(?P<id>\d+)/)?$", views.index, name="index"),
    url(r"^good/(?P<id>\d+)/$", views.good, name='good'),
    url(r"^categories/$", views.categories, name='categories'),
    url(r"^categories/(?P<id>\d+)/$", views.index, name='index'), # Это мой урл к контролеру 

]