<<<<<<< HEAD
# Generated by Django 4.1.4 on 2022-12-28 15:25
=======
# Generated by Django 4.1.4 on 2022-12-28 14:47
>>>>>>> 1b94d795ab6c1133cf75b268cff56f1a54afcdfa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_customuser_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(default='email', max_length=300, unique=True),
        ),
    ]
