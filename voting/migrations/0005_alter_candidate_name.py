# Generated by Django 4.1 on 2022-08-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0004_remove_candidate_photo_link_alter_voterlist_voted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="name",
            field=models.CharField(max_length=40),
        ),
    ]
