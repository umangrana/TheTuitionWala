# Generated by Django 3.0 on 2019-12-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=50)),
                ('stream', models.CharField(max_length=50)),
                ('studentID', models.IntegerField(unique=True)),
                ('email', models.URLField(unique=True)),
            ],
        ),
    ]