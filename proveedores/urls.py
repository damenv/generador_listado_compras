from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ProveedorListView.as_view(),
        name="proveedor-list"
    ),
    path(
        "proveedor/crear",
        views.ProveedorCreateView.as_view(),
        name="proveedor-create"
    ),
    path(
        "proveedor/<int:pk>/actualizar",
        views.ProveedorUpdateView.as_view(),
        name="proveedor-update"
    ),
    path(
        "proveedor/<int:pk>/eliminar",
        views.ProveedorDeleteView.as_view(),
        name="proveedor-delete"
    ),
    path(
        "proveedor/<int:pk>",
        views.ProveedorDetailView.as_view(),
        name="proveedor-detail"
    ),
    path("upload-csv/", views.upload_csv, name='proveedor-csv'),
]