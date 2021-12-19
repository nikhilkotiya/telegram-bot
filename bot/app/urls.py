from django.urls import path
from .views import ContactCreateAPI
from . import views
urlpatterns = [
    path('',ContactCreateAPI.as_view()),
    path('s/',views.apidata),
    # path('admin/', admin.site.urls),
]