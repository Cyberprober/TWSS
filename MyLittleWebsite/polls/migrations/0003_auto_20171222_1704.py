# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171221_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, '待教务员审核'), (1, '待教师确认'), (2, '已确认/已审核'), (3, '驳回待修改')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='teacher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_teacher', to='polls.Profile'),
        ),
    ]
