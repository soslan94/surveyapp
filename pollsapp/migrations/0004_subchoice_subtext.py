# Generated by Django 5.0.1 on 2024-02-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0003_alter_subchoice_suboption'),
    ]

    operations = [
        migrations.AddField(
            model_name='subchoice',
            name='subtext',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
