from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun),
    path('fun2',views.fun2),
    path('fun3/<d>',views.fun3),
    path('fun4',views.fun4),
    path('fun5/<d>',views.fun5),
    path('fun6',views.fun6.as_view()),
    path('fun7/<d>',views.fun7.as_view()),
    path('fun8',views.genericapiview.as_view()),
    path('fun9/<id>',views.update.as_view())

]