# Generated by Django 3.0 on 2019-12-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("posts", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(name="post", options={"ordering": ("-timestamp",)})
    ]
