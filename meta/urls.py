from django.urls import path

from meta.views import MetaDataCreateView, MetaDataDeleteView, MetaDataDetailView, MetaDataListView, MetaDataUpdateView


urlpatterns = [
    path("meta-data/",MetaDataListView.as_view(),name="metadata_list"),   
    path("meta-data/<int:pk>/", MetaDataDetailView.as_view(), name="metadata_detail"),
    path("meta-data/create/", MetaDataCreateView.as_view(), name="metadata_create"),
    path("meta-data/<int:pk>/update/", MetaDataUpdateView.as_view(), name="metadata_update"),
    path("meta-data/delete", MetaDataDeleteView.as_view(), name="metadata_delete"), 
]


