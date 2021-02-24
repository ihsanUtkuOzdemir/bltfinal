from django.contrib import admin
from django.urls import path,include
from accounts.views import login_view,register_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name="accounts"),
    path('',register_view, name="accounts"),
    path('exam/',include('exam.urls')),
    path('accounts/',include('accounts.urls')),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
