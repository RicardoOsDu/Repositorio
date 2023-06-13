from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from candidato.views import CandidatoUpdate, CandidatoList, CandidatoCreate



urlpatterns = [

      
    path("candidato_list/", CandidatoList.as_view(), name="candidato_list"),
    path("candidato_create/", CandidatoCreate.as_view(), name="candidato_create"),
    path("candidato_edit/<str:pk>/",CandidatoUpdate.as_view(), name="candidato_edit"),
     
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)