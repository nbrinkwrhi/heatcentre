from django.core.management.base import BaseCommand
import pandas as pd
from core.models import Variable

class Command(BaseCommand):
    help = 'Import variables from an Excel file'

    def handle(self, *args, **kwargs):
        # Path to your Excel file
        file_path = './heatcentre/core/data/HEAT_Master_Codebook.xlsx'

        # Load the Excel data
        excel_data = pd.read_excel(file_path)
     
        
            # Iterate through the DataFrame and create Variable instances
        for _, row in excel_data.iterrows():
            try:
                Variable.objects.create(
                    name=row['Variable Name'],
                    description=row['Description'],
                    unit=row['Unit']  # Adjust as per your Excel file's structure
                )
                self.stdout.write(self.style.SUCCESS(f"Successfully added variable {row['Variable Name']}"))
            except:
                self.stdout.write(self.style.ERROR(f"Failed to add variable {row['Variable Name']}"))

