"""instaDemo URL Configuration

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

from django.urls import path
from insta.views import helloWorldView, postView, postDetailView, postCreateView, postEditView, postDeleteView


urlpatterns = [
    path('', helloWorldView.as_view(), name='home'),
    path('posts', postView.as_view(), name='posts'),
    path('post/<int:pk>', postDetailView.as_view(), name='post_detail'),
    path('post/add', postCreateView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', postEditView.as_view(), name='edit_title'),
    path('post/delete/<int:pk>', postDeleteView.as_view(), name='post_delete')
]
