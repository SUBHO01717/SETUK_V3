# Generated by Django 4.2.11 on 2024-05-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0022_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('Installer ', 'Installer '), ('Reseller', 'Reseller')], default=None, max_length=10)),
                ('post_code', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('about_company', models.TextField(max_length=255)),
            ],
        ),
    ]