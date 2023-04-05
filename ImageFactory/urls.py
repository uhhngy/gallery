"""ImageFactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from main_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('illustration/',views.IllustrationView.as_view(),name="illustration"),
    path('illustration_filter/',views.IllustrationFilterView.as_view(),name="illustration_filter"),
    path('illustration_detail/<str:pk>/',views.IllustrationDetailView.as_view(),name="illustration_detail"),
    path('upload_illustration/',views.UploadIllustrationView.as_view(),name="upload_illustration"),
    path('text/',views.TextView.as_view(),name="text"),
    path('text_filter/',views.TextFilterView.as_view(),name="text_filter"),
    path('text_detail/<str:pk>/',views.TextDetailView.as_view(),name="text_detail"),
    path('upload_text/',views.UploadTextView.as_view(),name="upload_text"),
    path('add_count/',views.AddCountView.as_view(),name="add_count"),
    path('', include('image_generator.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
