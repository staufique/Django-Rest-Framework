from rest_framework import serializers
from .models import Student


def validate_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should be start with r')
    
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[validate_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance

    # def validate_roll(self, value):
    #     if value>=200:
    #         raise serializers.ValidationError("Seat is Full")
    #     return value

    # def validate(self,data):
    #     nm = data.get('name')
    #     ct = data.get('city')

    #     if nm.lower()=='shaikh2' and ct.lower() !='mumbai':
    #         raise serializers.ValidationError('Conditions not matched')
    #     return data
    
