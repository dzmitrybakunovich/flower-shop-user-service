from rest_framework import serializers


class NotifySerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    recipients_list = serializers.ListField(
        child=serializers.UUIDField(),
        required=True,
    )
    carbon_copy_list = serializers.ListField(
        child=serializers.UUIDField(),
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
