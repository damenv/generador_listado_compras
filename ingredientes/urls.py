from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.IngredienteListView.as_view(),
        name="ingrediente-list"
    ),
    path(
        "ingrediente/crear",
        views.IngredienteCreateView.as_view(),
        name="ingrediente-create"
    ),
    path(
        "ingrediente/<slug:pk>/actualizar",
        views.IngredienteUpdateView.as_view(),
        name="ingrediente-update"
    ),
    path(
        "ingrediente/<slug:pk>/eliminar",
        views.IngredienteDeleteView.as_view(),
        name="ingrediente-delete"
    ),
    path(
        "ingrediente/<slug:pk>",
        views.IngredienteDetailView.as_view(),
        name="ingrediente-detail"
    ),
    path("upload-csv/", views.upload_csv, name='ingrediente-csv'),
]