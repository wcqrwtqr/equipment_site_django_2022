# Generated by Django 4.0.5 on 2022-07-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_jobsdb_get_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsdb',
            name='file_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
