# Generated by Django 4.2.4 on 2023-09-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]