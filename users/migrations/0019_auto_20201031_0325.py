# Generated by Django 3.0.10 on 2020-10-30 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_patient_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('delivered', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='labtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('price', models.FloatField()),
                ('available', models.IntegerField()),
                ('cp', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='pathologist',
            name='PathoAddress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pathologist',
            name='PathoName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pathologist',
            name='Pathoimage',
            field=models.ImageField(blank=True, null=True, upload_to='pathology'),
        ),
        migrations.AlterField(
            model_name='pathologist',
            name='phone',
            field=models.CharField(max_length=98, null=True),
        ),
        migrations.AlterField(
            model_name='pathologist',
            name='qualification',
            field=models.CharField(max_length=98, null=True),
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.BookTest')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.labtest')),
            ],
        ),
        migrations.AddField(
            model_name='labtest',
            name='Pathologist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Pathologist'),
        ),
        migrations.CreateModel(
            name='AnonyTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Pathologist')),
            ],
        ),
        migrations.CreateModel(
            name='AddTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.AnonyTests')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.labtest')),
            ],
        ),
    ]