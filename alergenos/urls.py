from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.AlergenoListView.as_view(),
        name="alergeno-list"
    ),
    path(
        "alergeno/crear",
        views.AlergenoCreateView.as_view(),
        name="alergeno-create"
    ),
    path(
        "alergeno/<int:pk>/actualizar",
        views.AlergenoUpdateView.as_view(),
        name="alergeno-update"
    ),
    path(
        "alergeno/<int:pk>/eliminar",
        views.AlergenoDeleteView.as_view(),
        name="alergeno-delete"
    ),
    path(
        "alergeno/<int:pk>",
        views.AlergenoDetailView.as_view(),
        name="alergeno-detail"
    ),
    path("upload-csv/", views.upload_csv, name='alergeno-csv'),
]