from django.urls import path
from . import views

urlpatterns = [
    path("", views.ElaboracionListView.as_view(), name="elaboracion-list"),
    path(
        "elaboracion/crear",
        views.ElaboracionCreateView.as_view(),
        name="elaboracion-create"
    ),
    path(
        "elaboracion/<slug:pk>/actualizar",
        views.ElaboracionUpdateView.as_view(),
        name="elaboracion-update"
    ),
    path(
        "elaboracion/<slug:pk>/eliminar",
        views.ElaboracionDeleteView.as_view(),
        name="elaboracion-delete"
    ),
    path("elaboracion/<int:pk>",
         views.ElaboracionDetailView.as_view(),
         name="elaboracion-detail"),
    path("upload-csv/", views.upload_csv, name='elaboracion-csv'),
]