from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    Genero=((1, "Masculino"),
            (2, "Femenino"),
            (3, "Otro"),)

    documento=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    nacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=Genero)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='profile'


class Eps(models.Model):
    Regimen = ((1, "Subsidiado"),
               (2, "Contributivo"), )
    eps = models.CharField(max_length=50)
    regimen = models.SmallIntegerField(choices=Regimen)

    class Meta:
        db_table = 'eps'

    def __str__(self):
        return self.eps


class Medico(models.Model):
    especialidad=models.CharField(max_length=50)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class meta:
        db_table='medico'

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Paciente(models.Model):
    Vinculacion = ((1, "Cotizante"),
                   (2, "Beneficiario"),)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    eps=models.ForeignKey(Eps, on_delete=models.PROTECT)
    vinculacion=models.SmallIntegerField(choices=Vinculacion)

    class Meta:
        db_table='paciente'

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Citamedica(models.Model):
    Estado=((1, "Aprobada"),
            (2, "Rechazada"),
            (3,"Ejecutada"),)
    Pago=((1, "Si"),
          (2, "No"),)
    tipocita=models.CharField(max_length=50)
    estado=models.SmallIntegerField(choices=Estado)
    fecha=models.DateTimeField()
    costo=models.FloatField()
    pago=models.SmallIntegerField(choices=Pago)
    descripcion = models.CharField(max_length=250)
    medico=models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente=models.ForeignKey(Paciente, on_delete=models.PROTECT)

    class Meta:
        db_table='citamedica'