# Generated by Django 3.0 on 2020-01-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionWala', '0021_auto_20200121_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teaching_form',
            old_name='Subject_1_Fee',
            new_name='Average_Fee_Per_Subject',
        ),
        migrations.RenameField(
            model_name='teaching_form',
            old_name='Subject_1',
            new_name='Subjects',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_2',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_2_Fee',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_3',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_3_Fee',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_4',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_4_Fee',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_5',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_5_Fee',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_6',
        ),
        migrations.RemoveField(
            model_name='teaching_form',
            name='Subject_6_Fee',
        ),
    ]