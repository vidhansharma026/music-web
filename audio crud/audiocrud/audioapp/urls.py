from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="/"),
    path('delete/<pk>', views.delete, name="delete"),
    path('update/<int:uid>/', views.update, name="update"),
    path('updatedata/', views.updatedata, name="updatedata"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)