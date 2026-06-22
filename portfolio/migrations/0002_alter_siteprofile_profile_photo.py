from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteprofile',
            name='profile_photo',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
