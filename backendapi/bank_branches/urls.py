from django.urls import include,path
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('autocomplete',views.IFSCBankBranchesViewSet,basename='IFSCBank')
router.register('branches',views.SearchBankBranchesViewSet,basename='SearchBank')

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]