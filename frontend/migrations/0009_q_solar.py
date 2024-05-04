# Generated by Django 5.0.4 on 2024-05-04 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_q_boilerdata_name_q_evdata_name_q_heatpumps_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Q_Solar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_type', models.CharField(choices=[('Domestic', 'Domestic'), ('Commercial', 'Commercial')], default='Unspecified', max_length=255)),
                ('residency', models.CharField(choices=[('Detached', 'Detached'), ('Terrace', 'Terrace'), ('Bungalow', 'Bungalow'), ('Semidetached', 'Semidetached')], default='Unspecified', max_length=255)),
                ('ownership', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=255)),
                ('product', models.CharField(choices=[('Solar Panels', 'Solar Panels'), ('Solar Battery', 'Solar Battery'), ('Solar Pannels & Battery', 'Solar Pannels & Battery'), ('Not Sure', 'Not Sure')], default='Unspecified', max_length=255)),
                ('solar_exists', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=255)),
                ('building_type', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=255)),
                ('bed_rooms', models.CharField(max_length=255)),
                ('kws_usages', models.CharField(max_length=255)),
                ('monthly_usages', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Unspecified', max_length=255)),
                ('avg_electricity_bill', models.CharField(max_length=255)),
                ('roof_direction', models.CharField(choices=[('North', 'North'), ('Northwest', 'Northwest'), ('Northeast', 'Northeast'), ('East', 'East'), ('South', 'South'), ('Southeast', 'Southeast'), ('Southwest', 'Southwest'), ('West', 'West'), ('Not Sure', 'Not Sure')], default='Unspecified', max_length=255)),
                ('roof_window', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Unspecified', max_length=255)),
                ('roof_shadow_impact', models.CharField(choices=[('None', 'None'), ('Yes,Nearby Building', 'Yes,Nearby Building'), ('Yes,Nearby Tree', 'Yes,Nearby Tree'), ('Yes,Others', 'Yes,Others')], default='Unspecified', max_length=255)),
                ('pitch_type', models.CharField(choices=[('Flat', 'Flat'), ('Pitched / Angled', 'Pitched / Angled'), ('Others', 'Others'), ('Not Sure', 'Not Sure')], default='Unspecified', max_length=255)),
                ('installation_duration', models.CharField(choices=[('ASAP', 'ASAP'), ('Within 1 month', 'Within 1 month'), ('Within 3 months', 'Within 3 months'), ('Within 6 months', 'Within 6 months')], default='Unspecified', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('full_address', models.CharField(blank=True, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('formType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.q_formtype')),
            ],
        ),
    ]