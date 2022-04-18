from rest_framework import serializers


class NotifySerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipients_list = serializers.ListField(
        child=serializers.UUIDField(),
    )
    carbon_copy_list = serializers.ListField(
        child=serializers.UUIDField(),
        required=False,
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
