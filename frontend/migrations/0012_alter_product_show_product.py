# Generated by Django 4.2.11 on 2024-05-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_q_window'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='show_product',
            field=models.CharField(choices=[('YES', 'YES'), ('No', 'No')], default='YES', max_length=3),
        ),
    ]