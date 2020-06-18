from django.contrib import admin
from .models import Custom_Run_JobHistory,CustomJobInformations,TalendJobInformations,Talend_Run_JobHistory,Contacts,index_data,MatJobInformation,MatillionJobInformation,Matilion_Run_JobHistory,PythonJobInformations,Python_Run_JobHistory
# Register your models here.

admin.site.register(Contacts)

admin.site.register(index_data)
admin.site.register(MatJobInformation)
admin.site.register(MatillionJobInformation)
admin.site.register(Matilion_Run_JobHistory)
admin.site.register(PythonJobInformations)
admin.site.register(Python_Run_JobHistory)
admin.site.register(TalendJobInformations)
admin.site.register(Talend_Run_JobHistory)
admin.site.register(CustomJobInformations)
admin.site.register(Custom_Run_JobHistory)


