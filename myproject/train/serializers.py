from rest_framework import serializers

from .models import Train, Carriage, TrainUnit


class TrainSerializer(serializers.ModelSerializer):
    previous_unit = serializers.PrimaryKeyRelatedField(queryset=TrainUnit.objects.all(), allow_null=True, required=False)
    next_unit = serializers.PrimaryKeyRelatedField(queryset=TrainUnit.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Train
        fields = [
            'id',
            'name',
            'number',
            'previous_unit',
            'next_unit',
            'departure',
            'arrival',
            'departure_time',
            'arrival_time',
            'image',
        ]
        read_only_fields = ['id']


class CarriageSerializer(serializers.ModelSerializer):
    previous_unit = serializers.PrimaryKeyRelatedField(queryset=TrainUnit.objects.all(), allow_null=True, required=False)
    next_unit = serializers.PrimaryKeyRelatedField(queryset=TrainUnit.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Carriage
        fields = [
            'id',
            'name',
            'number',
            'previous_unit',
            'next_unit',
            'image',
        ]
        read_only_fields = ['id']
