from rest_framework import serializers
from .models import MainTable
from rest_framework import renderers


class MainTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTable
        fields = (
            'service_provider_name', 'response_code', 'error_message', 'account_number'
        )

# class CustomRenderer(renderers.JSONRenderer):
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response_data = {"response_code": data,}
#         return super().render(response_data, accepted_media_type, renderer_context)
