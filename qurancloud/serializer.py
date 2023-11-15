from rest_framework.serializers import ModelSerializer
from .models import *

class EditionSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = "__all__"

class SurahSerializer(ModelSerializer):
    class Meta:
        model = Surah
        fields = "__all__"


class AyahSerializer(ModelSerializer):
    surah = SurahSerializer()
    edition = EditionSerializer()
    class Meta:
        model = Ayah
        fields = ["number","text","number_in_surah","juz","manzil","page","ruku","hizb_quarter","sajda","audio","audio_secondary","surah","edition"]


class JuzSerializer(ModelSerializer):
    ayahs = AyahSerializer(many=True)
    surahs = SurahSerializer(many=True)
    edition = EditionSerializer()
    class Meta:
        model = Juz
        fields = "__all__"