
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from .models import DigitRecognition
import io
from PIL import Image




@api_view(["POST"])
def digit_predict(request):
    file_uploaded =  request.FILES.get('file_uploaded')
    if not file_uploaded:
        return Response({"error":"file_uploaded is required"})
    try:
        imgClassifierClass = DigitRecognition()
        img = Image.open(file_uploaded, mode='r')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        imShape = imgClassifierClass.readImage(img_byte_arr.getvalue())
        return Response(imShape)
    except Exception as e:
        print(e)
        return Response('found error')
    

