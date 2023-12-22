from django.contrib import admin
from .models import Variable

# Register your models here.

# Register your models here.
from .models import VariableData, Variable, Location, ClimateData, Study

admin.site.register(VariableData)
admin.site.register(Variable)
admin.site.register(Location)
admin.site.register(ClimateData)
admin.site.register(Study)
