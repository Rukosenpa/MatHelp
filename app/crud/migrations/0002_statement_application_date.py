# Generated by Django 3.0.3 on 2020-05-06 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_statementcategory_necessarily_paying'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='application_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 6, 12, 59, 5, 545878, tzinfo=utc), verbose_name='Дата Подачи'),
        ),
    ]