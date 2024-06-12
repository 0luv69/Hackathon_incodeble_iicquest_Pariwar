# Generated by Django 5.0.6 on 2024-06-12 11:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_issuemodel_got_relation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.issuemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to='main_app.profilemodel')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.relationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.issuemodel')),
                ('replied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='relationmodel',
            name='replied_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.replymodel'),
        ),
    ]
