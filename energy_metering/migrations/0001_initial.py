# Generated by Django 2.2 on 2019-09-17 15:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comunitaria', '0048_paymentsubscription_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('concept', models.CharField(max_length=350)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_confirmation', models.CharField(blank=True, default='', max_length=350, null=True)),
                ('payment_req', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('apitoshi_payment_id', models.CharField(blank=True, default='', max_length=600, null=True)),
                ('paid', models.BooleanField(blank=True, default=False)),
                ('payer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comunitaria.UserCommunity')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedEnergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('energy_amount', models.DecimalField(decimal_places=3, max_digits=20)),
                ('mam_address', models.CharField(max_length=300)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunitaria.Community')),
            ],
        ),
        migrations.CreateModel(
            name='EnergyTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('concept', models.CharField(max_length=350)),
                ('energy_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('consumer_community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumed_energy', to='comunitaria.Community')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='energy_metering.EnergyInvoice')),
                ('producer_community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pruduced_energy', to='comunitaria.Community')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumedEnergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('energy_amount', models.DecimalField(decimal_places=3, max_digits=20)),
                ('mam_address', models.CharField(max_length=300)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('processed', models.BooleanField(blank=True, default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunitaria.Community')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='energy_metering.EnergyInvoice')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='comunitaria.UserCommunity')),
            ],
        ),
        migrations.CreateModel(
            name='CommunityEnergyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apitoshi_apikey', models.CharField(blank=True, default='', max_length=350, null=True)),
                ('invoice_self_consumption', models.BooleanField(blank=True, default=False)),
                ('in_community_energy_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ex_community_energy_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('token', models.UUIDField(default=uuid.uuid4)),
                ('community', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comunitaria.Community')),
            ],
        ),
    ]
