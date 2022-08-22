from django.db import models
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)      
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class (models.Model):
    логин = models.CharField(db_column='Логин', unique=True, max_length=255)  # Field name made lowercase.
    пароль = models.TextField(db_column='Пароль')  # Field name made lowercase.
    id_покупатели = models.ForeignKey(, models.DO_NOTHING, db_column='id_Покупатели', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'авторизация'


class (models.Model):
    адреса_сыроварен = models.TextField(db_column='Адреса_сыроварен')  # Field name made lowercase.      

    class Meta:
        managed = False
        db_table = 'адреса сыроварен'


class (models.Model):
    адрес_доставки = models.TextField(db_column='Адрес_доставки')  # Field name made lowercase.
    дата = models.DateField(db_column='Дата')  # Field name made lowercase.
    доставлен = models.IntegerField(db_column='Доставлен')  # Field name made lowercase.
    коментарий = models.TextField(db_column='Коментарий', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'доставка'


class (models.Model):
    id_номенклатура = models.ForeignKey(, models.DO_NOTHING, db_column='id_Номенклатура')  # Field name made lowercase.
    id_покупателя = models.ForeignKey(, models.DO_NOTHING, db_column='id_Покупателя')  # Field name made 
lowercase.
    объем_покупки = models.IntegerField(db_column='Объем_покупки')  # Field name made lowercase.
    id_адрес_доставки = models.ForeignKey(, models.DO_NOTHING, db_column='id_Адрес_доставки')  # Field name made lowercase.
    дата_и_время = models.DateTimeField(db_column='Дата_и_время')  # Field name made lowercase.
    коментарий = models.IntegerField(db_column='Коментарий', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'заказы'


class (models.Model):
    id_покупатели = models.ForeignKey(, models.DO_NOTHING, db_column='id_Покупатели')  # Field name made 
lowercase.
    id_номенклатура = models.ForeignKey(, models.DO_NOTHING, db_column='id_Номенклатура')  # Field name made lowercase.
    объем_покупки = models.IntegerField(db_column='Объем_покупки')  # Field name made lowercase.
    дата = models.DateField(db_column='Дата')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'корзина'


class (models.Model):
    id = models.IntegerField(primary_key=True)
    название = models.TextField(db_column='Название')  # Field name made lowercase.
    доступность_товара = models.IntegerField(db_column='Доступность_товара')  # Field name made lowercase.
    тип_сыра = models.TextField(db_column='Тип_сыра', blank=True, null=True)  # Field name made lowercase.
    коментарий = models.TextField(db_column='Коментарий', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'номенклатура'


class (models.Model):
    фио = models.CharField(db_column='ФИО', max_length=255)  # Field name made lowercase.
    почта = models.TextField(db_column='Почта')  # Field name made lowercase.
    номер_телефона = models.CharField(db_column='Номер_телефона', max_length=20)  # Field name made lowercase.
    guid = models.TextField(db_column='Guid', blank=True, null=True)  # Field name made lowercase.       

    class Meta:
        managed = False
        db_table = 'покупатели'


class (models.Model):
    id_номенклатура = models.ForeignKey(, models.DO_NOTHING, db_column='id_Номенклатура')  # Field name made lowercase.
    объем_производства = models.IntegerField(db_column='Объем_производства')  # Field name made lowercase.
    дата_производства = models.DateField(db_column='Дата_производства')  # Field name made lowercase.    
    id_адреса_сыроварен = models.ForeignKey(, models.DO_NOTHING, db_column='id_Адреса_сыроварен')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'производство'


    id_номенклатура = models.ForeignKey(, models.DO_NOTHING, db_column='id_Номенклатура')  # Field name made lowercase.
    единица_измерения = models.TextField(db_column='Единица_измерения')  # Field name made lowercase.
    цена_за_единицу = models.IntegerField(db_column='Цена_за_единицу')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'цена'