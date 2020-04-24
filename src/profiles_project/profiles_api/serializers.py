from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ serializers a name fireld for testing our APIView"""

    name = serializers.CharField(max_length=10)
