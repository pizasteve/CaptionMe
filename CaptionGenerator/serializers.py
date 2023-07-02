from rest_framework import serializers

class CaptionGeneratorSerializer(serializers.Serializer):
    caption=serializers.CharField()