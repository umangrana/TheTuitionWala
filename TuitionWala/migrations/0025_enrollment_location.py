# Generated by Django 3.0 on 2020-01-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0024_auto_20200121_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='Location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
