from django.contrib import admin
from example.models import MyText, Place, Author

admin.site.register(MyText)
admin.site.register(Place)
admin.site.register(Author)
# Register your models here.
