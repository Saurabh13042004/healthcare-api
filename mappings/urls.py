from django.urls import path
from .views import MappingCreateView, MappingListView, MappingDetailView, MappingDeleteView

urlpatterns = [
    path('', MappingListView.as_view(), name='mapping-list'),
    path('create/', MappingCreateView.as_view(), name='mapping-create'),
    path('<int:patient_id>/', MappingDetailView.as_view(), name='mapping-detail'),
    path('delete/<int:id>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
