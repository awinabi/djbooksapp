from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("book_list"))),
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
]
