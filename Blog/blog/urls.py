from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
	path("", views.home, name="home"),
	path("post/<int:pk>/", views.blog_explorer, name="explorer"),
	path("feed/", views.feed, name="feed"),
	path("about/", views.about, name="about"),
	path("contact/", views.contact, name="contact"),
	path("single/", views.single, name="single"),
	path("<int:pk>/<slug:slug>/", views.detail, name="detail"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)