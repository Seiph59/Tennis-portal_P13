# Generated by Django 2.2.3 on 2019-08-04 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateTimeField()),
                ('adult_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('child_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('adult_number', models.PositiveSmallIntegerField(default=0)),
                ('child_number', models.PositiveSmallIntegerField(default=0)),
                ('payment_date_time', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='registered',
            field=models.ManyToManyField(through='events.Registration', to='accounts.Profile'),
        ),
    ]