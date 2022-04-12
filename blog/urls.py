"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),

    #below is associated with templates/listing.html
    path("", core_views.listing, name="listing"),

    #below is associated with templates/views_blog.html
    path("view_blog/<int:blog_id>/", core_views.view_blog, name="view_blog"),

    #To see some of the HttpRequest attributes in action
    path("see_request/", core_views.see_request),

    #All user objects, including AnonymousUser, have some attributes that give you more information about the user.
    path("user_info/", core_views.user_info),
    
    #To see @login_required in action
    path("private_place/", core_views.private_place),

    #This allows you to take advantage of all of Django’s built-in authentication views
    path("accounts/", include("django.contrib.auth.urls")),

    #This test looks at the HttpRequest.user.is_staff attribute. If it’s True, then the test passes. 
    path("staff_place/", core_views.staff_place),
    
    #Messaging a Logged-In User
    path("add_messages/", core_views.add_messages),
]