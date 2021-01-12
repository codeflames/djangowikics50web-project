from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.detailpage, name="entry-detail")

    # path("error", views.errorpage, name="error_page")
]
