# Generated by Django 4.2.11 on 2024-05-11 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_rename_details_packages_package_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Q_Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('full_address', models.CharField(blank=True, max_length=255, null=True)),
                ('post_code', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pack_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.packages')),
            ],
        ),
    ]
