from django.contrib import admin
from projects.models import Project, Userstory, Usecase, Task

class UserstoriesInline(admin.StackedInline):
    model = Userstory
	
class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{"fields":	("name", "description", "client_name", "started_on", "initiator")})	
	]
	inlines = [UserstoriesInline]
	
admin.site.register(Project)

from projects.models import Userstory
admin.site.register(Userstory)

from projects.models import Usecase
admin.site.register(Usecase)

from projects.models import Task
admin.site.register(Task)