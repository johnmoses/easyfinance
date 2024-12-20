# Generated by Django 4.2.2 on 2024-12-03 14:51

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
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('pic', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('pic', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_helps', to='helps.category')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
