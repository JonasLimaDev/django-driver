from django.db import models
from datetime import datetime

# Create your models here.
class Arquivos(models.Model):
    autor = models.CharField(max_length=75,null=False,blank=False)
    
    nome_arquivo = models.CharField(max_length=200,null=False,blank=False)
    data_upload = models.DateField(null=False,blank=False,default=datetime.now)
    link_arquivo = models.CharField(max_length=250, null=False,blank=False)
    
    def __str__(self):
        return self.nome_arquivo

    class Meta:
        ordering = ('data_upload',)
