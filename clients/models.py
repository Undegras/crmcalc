from django.db import models
from django.contrib import admin
#from django.contrib.auth.models import User
from django.db.models.fields import *



class Credit_Type(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, blank=True, unique=True)
    name = models.CharField(verbose_name='Тип кредита', max_length=30, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'Тип кредита'
        verbose_name_plural = u'Типы кредитов'

class Status_client_Info(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_name = models.CharField('Статус клиента', max_length=30, null=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = u'Статус клиента'
        verbose_name_plural = u'Статус клиентов'

class Status_client_Creditor(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_name = models.CharField('Статус по кредитору', max_length=30, null=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = u'Статус по кредитору'
        verbose_name_plural = u'Статусы по кредитору'


class Clients(models.Model):
    # Model = Clients
    class Meta:
        db_table = "Clients"
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'



    sex_choise = [
                ('M', 'Муж'),
                ('F', 'Жен'),
                ('O', 'Другое'),
    ]

    client_id = models.IntegerField(verbose_name='ID Пользователя', unique=True)
    client_add_num = models.IntegerField(verbose_name='Номер п/п', null=True, default=0)
    client_name = models.CharField(verbose_name='Фамилия Имя Отчество', max_length=256)
    client_email = models.EmailField(verbose_name='E-mail')
    client_phone = models.CharField(verbose_name='№ телефона', max_length=12, default='')
    client_phone_work = models.CharField(verbose_name='№ телефона раб', max_length=12, default='')
    client_phone_other = models.CharField(verbose_name='№ телефона доп', max_length=12, default='')
    client_birthday = models.DateField(verbose_name='Дата рождения')
    client_passport = models.CharField(verbose_name='Паспорт', max_length=20, default='')
    client_sex = models.CharField(verbose_name='Пол', max_length=1, choices=sex_choise)
    client_status_info = models.ForeignKey(Status_client_Info, on_delete=models.CASCADE)
    client_status_creditor = models.ForeignKey(Status_client_Creditor, on_delete=models.CASCADE)

    def get_model_fields(model):
        return model._meta.fields

    def __str__(self):
        return self.client_name

    def format_date(self, obj):
        return obj.client_birthday.strftime('%d.%m.%Y')

    def get_model_name(model):
        return model._meta.verbose_name_plural

    format_date.short_description = 'Date'

class ClientsInline(admin.TabularInline):
    model = Clients

class ClientAdmin (admin.ModelAdmin):
    #list_display = [ field.name for field in Clients._meta.get_fields()]
    list_display = [field.name for field in Clients.get_model_fields(Clients)]
    #list_display = [ field.name for field in Clients._me ]
    #list_display = ('client_name', 'client_email', 'client_status_info')

    #date_hierarchy = 'client_birthday'

    # inlines = [
    #     ClientsInline,
    # ]
    #

    fieldsets = (
        ('Личные данные', {
            'fields': ('client_id', 'client_name', 'client_passport', 'client_birthday', 'client_sex')
        }),
        ('Контактыне данные', {
            'fields': ('client_email', 'client_phone', 'client_phone_work', 'client_phone_other')
        }),
        ('Статус клиента', {
             'fields': ('client_status_info', 'client_status_creditor')
        }),
    )

class Status_client_InfoAdmin (admin.ModelAdmin):
    #list_display = [field.name for field in Status_client_Info._meta.get_fields()]
    list_display = ('id', 'status_name',)

class Status_client_CreditorAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Status_client_Creditor._meta.get_fields()]
    list_display = ('id', 'status_name',)

class Credit_TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Clients, ClientAdmin)
admin.site.register(Status_client_Info, Status_client_InfoAdmin)
admin.site.register(Status_client_Creditor, Status_client_CreditorAdmin)
admin.site.register(Credit_Type, Credit_TypeAdmin)


