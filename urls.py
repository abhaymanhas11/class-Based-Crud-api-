from .import views
from django.urls import path

urlpatterns=[
    path('studentmanagement/',views.studentapi.as_view()),
    path('studentmanagement/<int:id>',views.studentapi.as_view())
]