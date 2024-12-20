# Generated by Django 4.2.2 on 2024-12-03 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('exchange', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('perform_order', models.BooleanField(blank=True, default=False)),
                ('priority', models.IntegerField(blank=True, default=1000, null=True)),
                ('maximum_allocation', models.FloatField(blank=True, null=True)),
                ('minimum_allocation', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_prices', to='stocks.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('short', models.BooleanField(default=False)),
                ('buy_price', models.FloatField(blank=True, null=True)),
                ('buy_time', models.DateTimeField(blank=True, null=True)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('sell_time', models.DateTimeField(blank=True, null=True)),
                ('buy_indicator', models.CharField(blank=True, max_length=100, null=True)),
                ('sell_indicator', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_orders', to='finance.account')),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_orders', to='stocks.stock')),
                ('strategy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_orders', to='stocks.strategy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
