# Generated by Django 3.2.9 on 2021-12-08 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'expense_category',
            },
        ),
        migrations.CreateModel(
            name='DepositCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deposit_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'deposit_category',
            },
        ),
        migrations.AddConstraint(
            model_name='expensecategory',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_expense_category'),
        ),
        migrations.AddConstraint(
            model_name='depositcategory',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique_deposit_category'),
        ),
    ]