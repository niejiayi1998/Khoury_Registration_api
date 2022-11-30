from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Grade)
admin.site.register(models.Term)
admin.site.register(models.Student)
admin.site.register(models.Advisor)
admin.site.register(models.Admin)
admin.site.register(models.Department)
admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.TicketStatus)
admin.site.register(models.Ticket)
admin.site.register(models.HistoryStatus)
admin.site.register(models.History)
