from django.contrib.auth.models import Permission
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


@api_view(['GET'])
def overview(request):
    api_urls = {
        'all_items': 'products/',
        'Add': '/add_product',
        'Update': 'product_details/<sku>',
        'Detail': 'product_details/<sku>',
        'Delete': 'delete_product/<sku>',
        'Publish': 'publish_product/<sku>',
        'UnPublish': 'unpublish_product/<sku>',
        'api-auth': 'api-auth/',
        'api-token': 'api/token/',
        'token-refresh': 'api/token/refresh/',

    }
    return JsonResponse(api_urls)


@api_view(['GET'])
def product_list(request):
    """
    List all products, or create a new product.
    """
    permissons = []
    for perm in Permission.objects.filter(user=request.user):
        permissons.append(str(perm).split("|")[1].strip())

    if request.method == 'GET' and "Can view product" in permissons:
        # print(str(Permission.objects.filter(user=request.user)))
        products = Product.objects.all()
        # products = Product.objects.values('pr_name','sku','id')
        serializer = ProductSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_product(request):
    print(request.method, "^^^^^^^^^^^^^^^^^^^^^^^^^")
    permissions = []
    for perm in Permission.objects.filter(user=request.user):
        permissions.append(str(perm).split("|")[1].strip())
    if request.method == 'POST' and "Can add product" in permissions:
        serializer = ProductSerializer(data=request.data)
        # print(serializer)
        if Product.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif "Can add product" not in permissions:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_product(request, sku):
    permissions = []
    for perm in Permission.objects.filter(user=request.user):
        permissions.append(str(perm).split("|")[1].strip())
    print(Product.objects.filter(sku=sku), "***********")
    if request.method == 'DELETE' and "Can delete product" in permissions:
        try:
            product = Product.objects.filter(sku=sku)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif "Can delete product" not in permissions:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def publish_product(request, sku):
    permissions = []
    for perm in Permission.objects.filter(user=request.user):
        print(perm)
        permissions.append(str(perm).split("|")[-1].strip())
    try:
        Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' and "Can Publish Product" in permissions:
        Product.objects.filter(sku=sku).update(publish_status=True)
        products = Product.objects.filter(sku=sku)
        # products = Product.objects.values('pr_name','sku','id')
        serializer = ProductSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)
    elif "Can Publish Product" not in permissions:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def unpublish_product(request, sku):
    permissions = []
    for perm in Permission.objects.filter(user=request.user):
        permissions.append(str(perm).split("|")[-1].strip())
    try:
        Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' and "Can Publish Product" in permissions:
        Product.objects.filter(sku=sku).update(publish_status=False)
        products = Product.objects.filter(sku=sku)
        # products = Product.objects.values('pr_name','sku','id')
        serializer = ProductSerializer(products, context={'request': request}, many=True)
        return Response(serializer.data)
    elif "Can Publish Product" not in permissions:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def product_detail(request, sku):
    """
    Retrieve, update or delete a product instance.
    """
    permissions = []
    for perm in Permission.objects.filter(user=request.user):
        permissions.append(str(perm).split("|")[1].strip())

    print(request.data)
    try:
        product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT' and "Can change product" in permissions:
        serializer = ProductSerializer(product, data=request.data, context={'request': request}, partial=True)
        print()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
