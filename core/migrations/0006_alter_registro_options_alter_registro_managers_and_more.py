# Generated by Django 4.0.4 on 2022-06-15 05:45

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0005_alter_producto_descripcionproducto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registro',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='registro',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='correoUsuario',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='nombre',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='passwordUsuario',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='nombreUsuario',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='apellidoMaterno',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='apellidoPaterno',
        ),
        migrations.AddField(
            model_name='registro',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='registro',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='registro',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='registro',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='registro',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='registro',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='registro',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
