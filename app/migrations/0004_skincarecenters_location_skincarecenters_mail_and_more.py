# Generated by Django 4.2 on 2023-06-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_skincarecenters'),
    ]

    operations = [
        migrations.AddField(
            model_name='skincarecenters',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skincarecenters',
            name='mail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skincarecenters',
            name='opening_hour',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skincarecenters',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='skincarecenters',
            name='contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='skincarecenters',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skincarecenters',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]