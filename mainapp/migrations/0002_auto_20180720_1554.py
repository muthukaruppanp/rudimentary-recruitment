# Generated by Django 2.0 on 2018-07-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Accept/Shortlist'), ('r', 'Reject')], max_length=128, null=True),
        ),
    ]
