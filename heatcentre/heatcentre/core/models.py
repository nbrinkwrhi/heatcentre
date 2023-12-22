from django.db import models

# Create your models here.

#add class for study data 
class Study(models.Model):
     name = models.CharField(max_length=255, unique = True)
     location = models.CharField(max_length=255,unique = True)
     study_PI = models.CharField(max_length=255,unique = True)

class Location(models.Model):
     latitude = models.IntegerField()
     longitude = models.IntegerField()

#definitely need more details here
class ClimateData(models.Model):
     temperature = models.IntegerField()
     date = models.DateTimeField()
     location = models.ForeignKey(Location, on_delete=models.CASCADE)

#can add more details here
class Variable(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
            verbose_name_plural = "Variables"

class VariableData(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE) #not sure of the best way to do this relationship, might be better to come from study class
    variable_name = models.ForeignKey(Variable, on_delete = models.CASCADE)
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    climate_data = models.ForeignKey(ClimateData, on_delete=models.CASCADE)
    def __str__(self):
        return f"Patient ID: {self.patient_id}, Variable: {self.variable_name}, Date: {self.date}, Location: {self.location} Value: {self.value}"
    class Meta:
            verbose_name_plural = "Variable Data"
    
