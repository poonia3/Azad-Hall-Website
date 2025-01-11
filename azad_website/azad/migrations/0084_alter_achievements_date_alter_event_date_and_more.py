
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0083_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',

            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 10, 12, 47, 45, 304917, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 10, 12, 47, 45, 304917, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',

            field=models.DateTimeField(default=datetime.datetime(2025, 1, 10, 12, 47, 45, 304917, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',

            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 1, 10, 12, 47, 45, 304917, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',

            field=models.DateTimeField(default=datetime.datetime(2025, 1, 10, 12, 47, 45, 304917, tzinfo=datetime.timezone.utc)),
        ),
    ]
