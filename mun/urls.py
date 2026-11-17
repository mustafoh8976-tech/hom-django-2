from django.urls import path
from .views import *

urlpatterns = [
    path('home/<str:name>/<int:goal>/<str:discrip>', home_view),
    path('hom1/<str:name>/<int:age>/<str:discrip>', hom1_view),
    path('hom2/<str:city>/<str:country>/', hom2_view),
    path('hom3/<str:name>/<int:goal>/<str:discrip>/<int:age>/<str:city>/<str:country>/',hom3_view),
    path('hom4/<str:name>/<int:goal>/<str:discrip>/<int:age>/<str:city>/<str:country>/<int:trofai>/',hom4_view),
]
