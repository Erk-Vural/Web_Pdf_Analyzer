# Generated by Django 3.2.9 on 2021-12-05 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_assistantinfo_author_coursename_juryinfo_keywords_semester_summary_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssistantInfo',
            new_name='MentorInfo',
        ),
        migrations.AlterModelTable(
            name='mentorinfo',
            table='MentorInfo',
        ),
    ]
