from rest_framework import serializers
from rest_framework_recaptcha import ReCaptchaField


class MySerializer(serializers.Serializer):
    recaptcha = ReCaptchaField(
        error_messages={
            "invalid-input-response": "reCAPTCHA token is invalid.",
        }
    )


    