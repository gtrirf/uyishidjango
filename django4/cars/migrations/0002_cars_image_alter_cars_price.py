# Generated by Django 5.0.4 on 2024-05-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.IntegerField(),
        ),
    ]
