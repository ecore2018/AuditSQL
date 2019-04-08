# Generated by Django 2.1.7 on 2019-03-28 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0013_auto_20190328_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLQueryLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('user', models.CharField(max_length=30, verbose_name='用户名')),
                ('host', models.CharField(max_length=128, verbose_name='目标数据库地址')),
                ('database', models.CharField(max_length=32, verbose_name='目标数据库')),
                ('envi', models.SmallIntegerField(default=1, verbose_name='环境')),
                ('query_sql', models.TextField(default='', verbose_name='查询SQL')),
                ('query_time', models.CharField(default='', max_length=128, verbose_name='查询时间，单位s')),
                ('query_status', models.CharField(default='', max_length=2048, verbose_name='查询状态，成功或失败的原因')),
                ('affect_rows', models.IntegerField(default=0, verbose_name='影响行数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='查询时间')),
            ],
            options={
                'verbose_name': 'MySQL查询日志',
                'verbose_name_plural': 'MySQL查询日志',
                'db_table': 'auditsql_sql_query_log',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MysqlRulesChain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('action', models.CharField(choices=[('allow', '允许')], max_length=32, verbose_name='允许规则')),
                ('schema', models.CharField(default='', max_length=128, verbose_name='库名')),
                ('table', models.CharField(default='*', max_length=128, verbose_name='表名')),
                ('comment', models.CharField(default='', max_length=255, verbose_name='规则')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MysqlConfig', verbose_name='主机')),
            ],
            options={
                'verbose_name': '规则链',
                'verbose_name_plural': '规则链',
                'db_table': 'auditsql_mysql_rules_chain',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MysqlRulesGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('name', models.CharField(default='', max_length=30, verbose_name='组名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('rule', models.ManyToManyField(to='query.MysqlRulesChain')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '规则组',
                'verbose_name_plural': '规则组',
                'db_table': 'auditsql_mysql_rules_group',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='mysqlruleschain',
            unique_together={('comment', 'schema', 'table')},
        ),
    ]