from django.urls import path

from lunar.views import LunarImageView

urlpatterns=[
    path('',LunarImageView.as_view()),
]