# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0017_votecount'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
