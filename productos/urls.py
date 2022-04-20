from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ProductoListView.as_view(),
        name="producto-list"
    ),
    path(
        "producto/crear",
        views.ProductoCreateView.as_view(),
        name="producto-create"
    ),
    path(
        "producto/<slug:pk>/actualizar",
        views.ProductoUpdateView.as_view(),
        name="producto-update"
    ),
    path(
        "producto/<slug:pk>/eliminar",
        views.ProductoDeleteView.as_view(),
        name="producto-delete"
    ),
    path(
        "producto/<slug:pk>",
        views.ProductoDetailView.as_view(),
        name="producto-detail"
    ),
]