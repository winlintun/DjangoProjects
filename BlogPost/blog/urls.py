from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path("", views.home, name="home"),
	path("<int:pk>/<slug:slug>/", views.detail, name="detail"),	
	path("<int:pk>/", views.create, name="create"),
	path("edit/<int:pk>/", views.edit, name="edit"),
	path("search/", views.search, name="search"),
	path("delete/<int:pk>/", views.delete, name="delete"),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)