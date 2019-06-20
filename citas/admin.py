from django.contrib import admin
from .models import User, Profile, Eps, Medico, Paciente, Citamedica
# Register your models here.

@admin.register(Citamedica)
class Admincitamedica(admin.ModelAdmin):
    list_display = ('tipocita', 'estado', 'fecha', 'costo', 'pago', 'descripcion','nombre_medico', 'nombre_paciente',)

    def nombre_medico(self, medicon):
        return "%s %s" % (medicon.medico.user.first_name, medicon.medico.user.last_name)

    def nombre_paciente(self, pacienten):
        return "%s %s" % (pacienten.paciente.user.first_name, pacienten.paciente.user.last_name)


@admin.register(Profile)
class Adminprofile(admin.ModelAdmin):
    list_display = ('documento', 'telefono', 'nacimiento', 'genero', 'user', 'full_name',)

    def full_name(self, profile):
        return "%s %s" % (profile.user.first_name, profile.user.last_name)


@admin.register(Eps)
class Admineps(admin.ModelAdmin):
    list_display = ('eps', 'regimen',)


@admin.register(Medico)
class Adminmedico(admin.ModelAdmin):
    list_display = ('especialidad', 'user', 'nombre_medico',)

    def nombre_medico(self, medicon):
        return "%s %s" % (medicon.user.first_name, medicon.user.last_name)


@admin.register(Paciente)
class Adminpaciente(admin.ModelAdmin):
    list_display = ('user', 'eps', 'nombre_paciente',)

    def nombre_paciente(self, pacienten):
        return "%s %s" % (pacienten.user.first_name, pacienten.user.last_name)