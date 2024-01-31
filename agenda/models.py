from django.db import models

# Create your models here.


class Usuario(models.Model):
    ROLES=(
        (1,"Administrador"),
        (2,"Empleado"),
        (3,"Usuario")
    )
    idUsuario=models.BigAutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    nombreUsuario=models.CharField(max_length=50)
    contrasena=models.CharField(max_length=50)
    rol=models.IntegerField(choices=ROLES,default=3)
    


    def __str__(self):
        return f"{self.nombre}"



class Cita(models.Model):
    idCita=models.BigAutoField( primary_key=True, blank=True)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateField()
    lugar=models.CharField(max_length=50)
    hora=models.TimeField()
    servicio=models.CharField(max_length=50)
    empleado=models.CharField(max_length=50)

    def __str__(self):  
        return f"FECHA: {self.fecha} Y HORA: {self.hora}"




class Servicio(models.Model):
    idServicio=models.BigAutoField(unique=True,primary_key=True)
    nombre=models.CharField(max_length=50)
    duracion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=240)
    precio=models.CharField(max_length=50)
    disponibilidad=models.CharField(max_length=50)
    

    def __str__(self):
        return f"SERVICIO: {self.nombre}"

class UsuarioServicio(models.Model):
    idUsuarioServicio=models.BigAutoField(primary_key= True,blank=True)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)


class Empleado(models.Model):
    idEmpleado=models.BigAutoField(unique=True, primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    cargo=models.CharField(max_length=50)
    salario=models.CharField(max_length=50)

    def __str__(self):
        return f"EMPLEADO: {self.nombre} {self.apellido}"

class servicioempleado(models.Model):
    idServicioEmpleado=models.BigAutoField(primary_key=True, blank= True)
    idServicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    idEmpleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    

class Pago(models.Model):
    idPago=models.BigAutoField(unique=True,primary_key=True)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaPago=models.DateField()
    monto=models.CharField(max_length=50)
    estadoPago=models.CharField(max_length=50)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    




