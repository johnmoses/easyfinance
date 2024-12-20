# Generated by Django 4.2.2 on 2024-12-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('pic', models.CharField(blank=True, max_length=50, null=True)),
                ('pic1', models.CharField(blank=True, max_length=50, null=True)),
                ('pic2', models.CharField(blank=True, max_length=50, null=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=True)),
                ('last_content', models.TextField(blank=True, max_length=100, null=True)),
                ('unread_messages', models.IntegerField(default=0)),
                ('starter_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatsUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('attachment', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_id', models.IntegerField(default=0)),
                ('sender_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
