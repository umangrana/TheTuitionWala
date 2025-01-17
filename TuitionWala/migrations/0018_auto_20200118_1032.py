# Generated by Django 3.0 on 2020-01-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0017_auto_20200118_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollmentform_table',
            name='Username',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrollmentform_table',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True),
        ),
    ]
