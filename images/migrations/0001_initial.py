# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import images.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=images.models.get_image_path)),
                ('thumbnail', models.ImageField(upload_to=images.models.get_image_path)),
            ],
        ),
    ]
