from rest_framework.serializers import Serializer, FileField

# Serializers define the API representation.

def required(value):
    if value is None:
        raise Serializer.ValidationError('This field is required')

class Digit_Prediction():
    def __init__(self,file_uploaded):
        self.file_uploaded = file_uploaded
    

class UploadSerializer(Serializer):
    file_uploaded = FileField(allow_empty_file=False)
    class Meta:
        fields = ['file_uploaded']
        
            




