# Generated by Django 4.1.4 on 2023-06-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_diseasedetail_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasedetail',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
