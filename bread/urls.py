from django.urls import path
from .views import BreadListView, BreadDetailView, BreadUpdateView, BreadDeleteView, BreadCreateView, BreadListAPI, BreadDetailAPI

urlpatterns = [
    path('', BreadListView.as_view(), name='bread-list'),
    path('<int:pk>/', BreadDetailView.as_view(), name='bread-detail'),
    path('<int:pk>/update/', BreadUpdateView.as_view(), name='bread-update'),
    path('<int:pk>/delete/', BreadDeleteView.as_view(), name='bread-delete'),
    path('create/', BreadCreateView.as_view(), name='bread-create'),
    path('api/v1/', BreadListAPI.as_view(), name='bread-list_api'),
    path('api/v1/<int:pk>', BreadDetailAPI.as_view(), name='bread-detail_api'),
]