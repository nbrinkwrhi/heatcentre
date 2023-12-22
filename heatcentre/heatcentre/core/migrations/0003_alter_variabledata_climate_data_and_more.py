# Generated by Django 4.2.8 on 2023-12-22 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_climatedata_location_study_variabledata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variabledata",
            name="climate_data",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.climatedata"),
        ),
        migrations.AlterField(
            model_name="variabledata",
            name="location",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.location"),
        ),
        migrations.AlterField(
            model_name="variabledata",
            name="study",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.study"),
        ),
    ]