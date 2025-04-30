from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response ({'status':200, 'payload':serializer.data})



class StudentAPI(APIView):

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)

        return Response({'status': 200, 'payload': serializer.data})



    def post(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass


































# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)

#     return Response({'status': 200, 'payload': serializer.data})


# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data = request.data)

#     if request.data['age']<18:
#         return Response({'status': 403, 'messages': "age must be greater than 18"})

#     if not serailizer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403,'errors': serializer.errors,  'message': data, 'message': 'Something went wrong'})
#     serializer.save()
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})
    
# #@api_view(['PUT'])
# #def update_student(request, id):
#     #try:
#         #student_obj = Student.Object.get(id = id)
#         #serializer = StudentSerializer(student_obj, data = request.data, partial = True)


# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = STudent.objects.get(id = id)
#         serializer = StudentSerializer(student_obj, data = request.data, partial = True)

#         # if request.data['age']<18:
#         #     return Response({'status': 403, 'messages': "age must be greater than 18"})

#         if not serailizer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403,'errors': serializer.errors,  'message': data, 'message': 'Something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalide id'})