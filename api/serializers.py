from rest_framework import serializers

from core.models import GrantGoal

class ListGrandGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = [
            "id",
            "ggname",
            "timestamp",
            "days_duration",
            "state",
            "status"
        ]
        
## DETAIL

class DetailGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = "__all__"
        
        
class CreateGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = "__all__"
        

class UpdateGrandGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = [
            "ggname",
            "description",
            "days_duration",
            "state",
            "priority",
            "status"
        ]