from rest_framework import serializers

class UserSerializer(serializers.Serializer):
  last_buy = serializers.IntegerField()
  times_buy = serializers.IntegerField()
  total_buyed = serializers.FloatField()
  userIdentifier = serializers.CharField()


class UpSellingSerializer(serializers.Serializer):
  cluster = serializers.IntegerField()
  subCluster = serializers.IntegerField(required = False)
  itemId = serializers.CharField(required = False)
  n= serializers.IntegerField(default=5)