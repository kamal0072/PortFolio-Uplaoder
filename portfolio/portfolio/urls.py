from django.contrib import admin
from django.urls import path
from apps import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PortView.as_view(),name='home'),
    path('<int:pk>',views.UserView.as_view(),name='info'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
