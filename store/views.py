from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Order
from .serializers import BookSerializer, OrderSerializer, UserSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Registered successfully'})
    return Response(serializer.errors)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'error'})
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request):  
     

    if request.method == 'GET':
        serializer = BookSerializer(Book)
        return Response(serializer.data)

    if request.method == 'PUT':
        if not request.user.is_authenticated:
            return Response({'error'})
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        if not request.user.is_staff:
            return Response({'error'})
        Book.delete()
        return Response({'Book deleted'})


@api_view(['GET', 'POST'])
def order_list(request):
    if not request.user.is_authenticated:
        return Response({'error'})

    if request.method == 'GET':
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
