# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150315_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(default=b'')),
                ('author', models.CharField(max_length=128)),
                ('category', models.CharField(default='\u672a\u5206\u7c7b', max_length=255, verbose_name='\u76ee\u5f55', db_index=True)),
                ('tags', models.CharField(default=b'', max_length=255, verbose_name='\u6807\u7b7e', blank=True)),
                ('is_commented', models.BooleanField(default=False, verbose_name='\u662f\u5426\u88ab\u8bc4\u8bba')),
                ('is_reshipped', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u8f6c\u8f7d')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Essay',
        ),
    ]
