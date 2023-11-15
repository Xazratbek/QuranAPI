from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import *

class EditionListView(ListAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    filterset_fields = ["format","language","type"]
    search_fields = ["identifier","name","englishName"]

class AyahListView(ListAPIView):
    queryset = Ayah.objects.all()
    serializer_class = AyahSerializer

class SurahListView(ListAPIView):
    queryset = Surah.objects.all()
    serializer_class = SurahSerializer

class JuzListView(ListAPIView):
    queryset = Juz.objects.all()
    serializer_class = JuzSerializer

class QuranEditionDetailView(RetrieveAPIView):
    lookup_field = "edition"

    def get_queryset(self):
        edition = self.kwargs.get("edition")
        data = Ayah.objects.filter(edition__identifier=edition)
        return data