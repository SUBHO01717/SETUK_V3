# Generated by Django 4.2.11 on 2024-05-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_alter_q_homesecurity_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_infraredheat',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='full_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='heating_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='ownership',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='post_code',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='q_infraredheat',
            name='residency',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='building_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='installation_duration',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='installation_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='monthly_usages',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='ownership',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='pitch_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='residency',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='roof_direction',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='roof_shadow_impact',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='roof_window',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='solar_exists',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='q_solar',
            name='solar_type',
            field=models.CharField(max_length=255),
        ),
    ]
