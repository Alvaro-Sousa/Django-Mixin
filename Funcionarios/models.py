from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class ClienteQuerySet(models.QuerySet):
    def activates(self):
        return self.filter(is_deleted=False)
    def deleted(self):
        return self.filter(is_deleted=True)

class ClienteManager(models.Manager):
    def get_queryset(self):
        return ClienteQuerySet(self.model, using=self.db)
    
    def active(self):
        return self.get_queryset().active()
    
    def deleted(self):
        return self.get_queryset().deleted()

class Cliente(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, unique=True)
    nascimento = models.DateField()
    objects = ClienteManager()

    #USEI IA PQ NÃO TAVA ENTENDO PQ KRALHOS NÃO ESTAVA APARECENDO BOTÃO DE
    #RESTAURAR AS COISAS APAGADAS
    def delete(self, *ars, **kwarsg):
        self.is_deleted = True
        self.save()
    
    def restored(self):
        self.is_deleted = False
        self.save()

    def __str__(self):
        return self.name
    