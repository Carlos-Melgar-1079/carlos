from django.urls import path
from kriks_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarproovedores/",views.registrarproovedores,name="registrarproovedores "),
    path("seleccionarproovedores/<codigo>",views.seleccionarproovedores,name="seleccionarproovedores"),
    path("editarproovedor/",views.editarproovedor,name="editarproovedor"),
    path("borrarproovedor/<codigo>",views.borrarproovedor,name="borrarproovedor"),
]