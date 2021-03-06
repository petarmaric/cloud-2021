# Generated by Django 3.2.9 on 2021-11-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'get_latest_by': 'visit_time', 'ordering': ['-visit_time']},
        ),
        migrations.AlterField(
            model_name='visit',
            name='user_ip',
            field=models.GenericIPAddressField(db_index=True, unpack_ipv4=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
