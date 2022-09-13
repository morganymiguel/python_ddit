"""SPA_EMP URL Configuration

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
from django.urls import path
from SPA_EMP import views


urlpatterns = [
    path('', views.emp),
    path('emp', views.emp),
    path('test2', views.test2),
    path('test3', views.test3),
    path('test4', views.test4),
    path('test5', views.test5),
    path('test6', views.test6),
    path('jqtest1', views.jqtest1),
    path('jqtest2', views.jqtest2),
    path('jqtest3', views.jqtest3),
    path('jqtest4', views.jqtest4),
    path('jqtest5', views.jqtest5),
    path('jqtest6', views.jqtest6),
    path('emp_list.ajax', views.emp_list_ajax),
    path('emp_detail.ajax', views.emp_detail_ajax),
    path('emp_insert.ajax', views.emp_insert_ajax),
    path('emp_update.ajax', views.emp_update_ajax),
    path('emp_delete.ajax', views.emp_delete_ajax),
    
]
