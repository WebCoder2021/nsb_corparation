from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    info  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return  self.name
class CompModel(models.Model):
    name = models.CharField(max_length=200)
    info  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return  self.name
class CPUBrand(models.Model):
    name = models.CharField(max_length=200)
    info  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return  self.name
class CPU(models.Model):
    brand = models.ForeignKey(CPUBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    chastota  = models.CharField(max_length = 100)
    yader  = models.CharField(max_length = 100)
    patok  = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return  str(self.brand) + self.name

class GPUBrand(models.Model):
    name = models.CharField(max_length=200)
    info  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return  self.name
class GPU(models.Model):
    brand = models.ForeignKey(CPUBrand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    size  = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return str(self.brand) + self.model


class Screen(models.Model):
    size = models.CharField(max_length=100)
    type  = models.CharField(max_length = 100,blank=True,null=True)
    chastota  = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.size + self.type + self.chastota

class DDRType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class DDR(models.Model):
    size = models.CharField(max_length=100)
    type  = models.ForeignKey(DDRType,on_delete=models.CASCADE)
    addition  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return self.size + str(self.type) + self.addition
class MemoryType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Memory(models.Model):
    size = models.CharField(max_length=100)
    type  = models.ForeignKey(MemoryType,on_delete=models.CASCADE)
    addition  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return self.size + str(self.type) + self.addition

class Connection(models.Model):
    name = models.CharField(max_length=100)
    addition  = models.CharField(max_length = 500,blank=True,null=True)

    def __str__(self) -> str:
        return self.name   
class Keyboard(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Corpus(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Color(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Camera(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Port(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class CompImages(models.Model):
    image = models.ImageField(upload_to='comp_images/%Y/%d')
class Computer(models.Model):
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE,blank=True,null=True)
    model = models.ForeignKey(CompModel,on_delete = models.CASCADE,blank=True,null=True)
    cpu = models.ForeignKey(CPU,on_delete = models.CASCADE,blank=True,null=True)
    gpu = models.ForeignKey(GPU,on_delete = models.CASCADE,blank=True,null=True)
    screen = models.ForeignKey(Screen,on_delete = models.CASCADE,blank=True,null=True)
    ddr = models.ForeignKey(DDR,on_delete = models.CASCADE,blank=True,null=True)
    memory = models.ManyToManyField(Memory)
    keyboard = models.ManyToManyField(Keyboard)
    connection = models.ManyToManyField(Connection)
    corpus = models.ForeignKey(Corpus,on_delete = models.CASCADE,blank=True,null=True)
    color = models.ForeignKey(Color,on_delete = models.CASCADE,blank=True,null=True)
    camera = models.ForeignKey(Camera,on_delete = models.CASCADE,blank=True,null=True)
    ports = models.ManyToManyField(Port)
    sale = models.PositiveSmallIntegerField(blank=True,null=True)
    images = models.ManyToManyField(CompImages)

    def __str__(self):
        return str(self.brand) + str(self.model)+ str(self.cpu)+ str(self.gpu)