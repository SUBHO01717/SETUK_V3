# Generated by Django 5.0.4 on 2024-05-04 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_blog_contact_packagecatgory_projects_q_formtype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_boilerdata',
            name='boiler_type',
            field=models.CharField(choices=[('Central Heating & Hot Water', 'Central Heating & Hot Water'), ('Central Heating Only', 'Central Heating Only'), ('Hot Water Only', 'Hot Water Only'), ('Do not Know', 'Do not Know')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='formType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frontend.q_formtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='full_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='job_type',
            field=models.CharField(choices=[('New Instalation', 'New Instalation'), ('Replacement', 'Replacement'), ('Service', 'Service'), ('Others', 'Others')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='post_code',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='power_usage',
            field=models.CharField(choices=[('Gas', 'Gas'), ('Oil', 'Oil'), ('LPG', 'LPG'), ('Others', 'Others')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_boilerdata',
            name='property_type',
            field=models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'Office'), ('Others', 'Others')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
