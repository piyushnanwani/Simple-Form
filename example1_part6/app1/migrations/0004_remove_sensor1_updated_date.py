# Generated by Django 2.1.7 on 2019-03-02 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20190302_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor1',
            name='updated_date',
        ),
    ]
