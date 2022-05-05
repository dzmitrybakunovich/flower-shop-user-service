from rest_framework import serializers


class FavoriteSerializer(serializers.Serializer):
    user_id = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
