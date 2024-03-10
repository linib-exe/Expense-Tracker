# Generated by Django 4.2.11 on 2024-03-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('amount', models.FloatField()),
                ('tx_type', models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], max_length=3)),
                ('remarks', models.TextField()),
                ('category', models.CharField(choices=[('Petrol', 'Petrol'), ('Food', 'Food'), ('Fees', 'Fees'), ('Recreation', 'Recreation')], max_length=20)),
                ('proof', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
