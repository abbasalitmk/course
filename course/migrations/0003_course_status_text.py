# Generated by Django 4.2.7 on 2023-11-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status_text',
            field=models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Enable', max_length=7),
        ),
    ]
