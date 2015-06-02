# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def migrate_users_emails(apps, schema_editor):

    EmailAddress = apps.get_model("account", "EmailAddress")
    Users = apps.get_model("main", "User")

    for users in Users.objects.all():
        EmailAddress.objects.create(
            user=users,
            email=users.email,
            verified=users.is_active,
            primary=True,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
    ]

    operations = [
        migrations.RunPython(migrate_users_emails),
    ]
