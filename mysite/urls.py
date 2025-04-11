
from django.contrib import admin
from django.urls import path
from django.urls import include
from polls import urls
urlpatterns = [
    path('tra/', include("polls.urls")),
    path('admin/', admin.site.urls),
]
