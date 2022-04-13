# Generated by Django 4.0.4 on 2022-04-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HkuMember',
            fields=[
                ('hku_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venuecode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('LT', 'Lecture Theatre'), ('CR', 'Classroom'), ('TR', 'Tutorial Room')], max_length=2)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('event', models.CharField(choices=[('I', 'Entry'), ('O', 'Exit')], max_length=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapi.hkumember')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapi.venue')),
            ],
        ),
        migrations.AddField(
            model_name='hkumember',
            name='venues',
            field=models.ManyToManyField(through='coreapi.Visit', to='coreapi.venue'),
        ),
    ]
