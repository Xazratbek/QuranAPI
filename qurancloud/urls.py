from django.urls import path
from .views import *

urlpatterns = [
    path("edition/",EditionListView.as_view(),name="edition-list"),
    path("ayah/",AyahListView.as_view(),name="ayah-list"),
    path("surah/",SurahListView.as_view(),name="surah-list"),
    path("juz/",JuzListView.as_view(),name="juz-list"),
    path("edition/<str:edition>/",QuranEditionDetailView.as_view(),name="edition-detail")
]
