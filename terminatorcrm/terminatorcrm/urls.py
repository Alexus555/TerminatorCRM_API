"""terminatorcrm URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from crm.views import *

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'supplier', SupplierViewSet)
router.register(r'client', ClientViewSet)
router.register(r'industry', IndustryViewSet)
router.register(r'contractor', ContractorViewSet)
router.register(r'product', ProductViewSet)
router.register(r'product_category', ProductCategoryViewSet)
router.register(r'project_type', ProjectTypeViewSet)
router.register(r'project_status', ProjectStatusViewSet)
router.register(r'member', MemberViewSet)
router.register(r'role', RoleViewSet)
router.register(r'project_team', ProjectTeamViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'contract', ContractViewSet)
router.register(r'lead', LeadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]