from django.contrib import admin
from .models import Guest
from .models import Enquiry
from .models import DatabaseInsert
from .models import Requirement

# Register your models here.
admin.site.register(Guest)
admin.site.register(Enquiry)
admin.site.register(DatabaseInsert)
admin.site.register(Requirement)
