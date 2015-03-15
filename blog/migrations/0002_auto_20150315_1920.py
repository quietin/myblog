# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='category',
            field=models.CharField(default='\u672a\u5206\u7c7b', max_length=255, verbose_name='\u76ee\u5f55', db_index=True),
        ),
        migrations.AlterField(
            model_name='essay',
            name='content',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='essay',
            name='tags',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
