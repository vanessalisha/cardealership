from django.urls import path
from. import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.home, name="home"),
    path('base/', views.base, name="base"),
	path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
   	path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('page/', views.page, name="page"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
