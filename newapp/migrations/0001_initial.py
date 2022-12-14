# Generated by Django 3.2.7 on 2022-10-11 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('mail_Id', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='url_list_de',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('imageUrl', models.URLField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('end_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
            ],
        ),
    ]
