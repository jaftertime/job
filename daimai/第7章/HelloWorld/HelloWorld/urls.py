"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import view
from . import access_db
xx=path('page1/', view.page1)
print('page1 path=',xx, type(xx))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', view.page1),
    path('page2/', view.page2),
    path('page3/', view.page3),
    path('page4/', view.page4),
    path('page5/', view.page5),
    path('add-data/', view.add_data),
    path('query-data/', view.query_data),
    path('filter-data/', view.filter_data),
    path('delete-data/', view.delete_data),
    path('update-data/', view.update_data),
    path('', view.index),
]
