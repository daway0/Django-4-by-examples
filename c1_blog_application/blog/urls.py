from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>", views.post_detail, name="post_detail"),
    path("2/<int:id>", views.post_detail2, name="post_detail2"),

]
