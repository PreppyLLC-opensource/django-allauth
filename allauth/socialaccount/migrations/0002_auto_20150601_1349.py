# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


PROVIDERS = {
    'vk-oauth': 'vk',
    'facebook': 'facebook',
    'twitter': 'twitter,'
}

def migrate_socialaccounts(apps, schema_editor):

    SocialAccount = apps.get_model("socialaccount", "SocialAccount")
    UserSocialAuth = apps.get_model("social_auth", "UserSocialAuth")

    for old_acc in UserSocialAuth.objects.all():
        SocialAccount.objects.create(
            user=old_acc.user,
            provider=PROVIDERS[old_acc.provider],
            uid=old_acc.uid,
            extra_data=old_acc.extra_data,
        )
    UserSocialAuth.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0001_initial'),
        ('social_auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(migrate_socialaccounts),
    ]
