# Generated by Django 3.2.18 on 2023-04-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_recipe_edited_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['publication_date']},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='edited_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
