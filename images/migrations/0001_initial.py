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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=images.models.get_image_path)),
            ],
        ),
    ]
