from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path("posts/<int:pk>/", views.home, name="feed"),
	path("<int:pk>/", views.blog_explorer, name="post"),
	path("", views.feed, name="home"),
	path("about/", views.about, name="about"),
	path("contact/", views.contact, name="contact"),
	path("single/<str:user>/", views.single, name="single"),
	path("<int:pk>/<slug:slug>/", views.detail, name="detail"),

	path("<int:userId>/edit/<int:postId>/", views.post_edit, name="edit"),
	path("<int:pk>/<slug:slug>/delete", views.post_delete, name="delete"),
	path("search/", views.search_post, name="search"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)