
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'email', 'password', 'user_type']  # Ajout du champ 'user_type'
        extra_kwargs = {
            'password': {'write_only': True},  # Pour que le champ mot de passe ne soit pas inclus dans la réponse
        }
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user_type = validated_data.pop("user_type")  # Récupérer le champ user_type
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
