# Generated by Django 4.0.4 on 2022-05-12 18:18

from django.db import migrations

def populate_usertype(apps, schemaeditor):
    user_types = {
        "reader": "A subsrciber to the newspaper",
        "journalist": "A staff member that creates content",
        "editor": "A staff member in charge of editing",
    }
    UserType = apps.get_model('accounts', 'UserType')
    for name, desc in user_types.items():
        user_type = UserType(name=name, description=desc)
        user_type.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(populate_usertype)
    ]