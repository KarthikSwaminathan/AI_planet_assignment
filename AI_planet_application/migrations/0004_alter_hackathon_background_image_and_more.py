# Generated by Django 4.1.7 on 2023-05-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_planet_application', '0003_alter_submission_file_alter_submission_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='background_image',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='hackathon_image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
