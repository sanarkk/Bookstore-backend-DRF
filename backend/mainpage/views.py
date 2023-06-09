from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import IsOwner, IsMyProfile
from .models import Book, Order, Profile
from .serializers import (
    BookSerializer,
    CreateBookSerializer,
    UpdateBookSerializer,
    OrderSerializer,
    UserProfileSerializer,
    UpdateUserProfileSerializer,
    UserListedBooksSerializer,
)


# Create your views here.
class ListBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(status=Book.BookStatus.ACTIVE)
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all books",
        operation_description="This API endpoint allows "
                              "user to list all the books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListFantasyBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.FANTASY
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all fantasy books",
        operation_description="This API endpoint allows "
                              "user to list all the fantasy books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListAdventureBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.ADVENTURE
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all adventure books",
        operation_description="This API endpoint allows "
                              "user to list all the adventure books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListRomanceBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.ROMANCE
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all romance books",
        operation_description="This API endpoint allows "
                              "user to list all the romance books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListDetectiveBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.DETECTIVE
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all detective books",
        operation_description="This API endpoint allows "
                              "user to list all the detective books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListThrillerBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.THRILLER
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all thriller books",
        operation_description="This API endpoint allows "
                              "user to list all the thriller books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListHistoricalBooksAPI(generics.ListAPIView):
    queryset = Book.objects.filter(
        status=Book.BookStatus.ACTIVE,
        genre=Book.BookGenre.HISTORICAL
    )
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('book_name', 'author__username')
    ordering_fields = ('price',)

    @swagger_auto_schema(
        name="List all historical books",
        operation_description="This API endpoint allows "
                              "user to list all the historical books.",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateBookAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Create a book",
        operation_description="This API endpoint allows "
                              "user to create a book.",
        tags=["Book"],
    )
    def post(self, request, *args, **kwargs):
        return self.create_book(request)

    def create_book(self, request):
        serializer = CreateBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = request.user.id
        serializer.save(author_id=user_id)
        print(serializer.data)
        message = _("Book created")
        return Response({f"{message}"}, status=status.HTTP_201_CREATED)


class RetrieveBookAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Get the book",
        operation_description="This API endpoint allows user to get a certain "
                              "book by ID.[only if an user is authenticated]",
        tags=["Book"],
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateBookAPI(generics.UpdateAPIView):
    queryset = Book.objects.all()
    lookup_field = "pk"
    serializer_class = UpdateBookSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    http_method_names = ["put"]

    @swagger_auto_schema(
        name="Update information about the book",
        operation_description="This API endpoint allows "
                              "user to update information "
                              "about the book.[only if an "
                              "user is authenticated]",
        tags=["Book"],
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True)
        message_updated = _("Book updated")
        message_not_updated = _("Book not updated")

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=self.request.user)
            return Response(
                {"Message": f"{message_updated}"},
                status=status.HTTP_200_OK
            )
        else:
            return Response({f"{message_not_updated}"})


class GetOrderAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "pk"

    @swagger_auto_schema(
        name="Get the order",
        operation_description="This API endpoint allows user to get the order "
                              "by ID.[only if an user is authenticated]",
        tags=["Order"],
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


class CreateOrderAPI(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        name="Create an order",
        operation_description="This API endpoint allows "
                              "user to create an order"
                              ".[only if an user is authenticated]",
        tags=["Order"],
    )
    def post(self, request, *args, **kwargs):
        return self.create_order(request)

    def create_order(self, request):
        instance = self.get_object()
        book = Book.objects.filter(id=instance.id)
        if instance.status == Book.BookStatus.ACTIVE:
            if instance.author == request.user:
                message = _("You cant but own book.")
                return Response(
                    {f"{message}"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED
                )
            serializer = OrderSerializer(instance,
                                         data=request.data)
            serializer.is_valid(raise_exception=True)
            user_id = request.user
            Order.objects.create(
                user=user_id,
                book=instance,
                phone_number=request.data["phone_number"],
                country=request.data["country"],
                delivery_address=request.data["delivery_address"],
            )
            book.update(status=Book.BookStatus.INACTIVE)
            message = _("Order created")
            return Response(
                {f"{message}"},
                status=status.HTTP_201_CREATED
            )
        else:
            message_2 = _("This book is inactive")
            return Response(
                {f"{message_2}"},
                status=status.HTTP_204_NO_CONTENT
            )


class ListUserInformation(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Get the user information",
        operation_description="This API endpoint allows "
                              "user to get information about his profile"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UpdateUserInformation(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]
    http_method_names = ["put"]

    @swagger_auto_schema(
        name="Update profile information",
        operation_description="This API endpoint allows "
                              "user to update information of his profile"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        serializer = self.serializer_class(profile, data=request.data)
        message_updated = _("User profile updated")
        message_not_updated = _("User profile not updated")

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({f"{message_updated}"}, status=status.HTTP_200_OK)
        else:
            return Response({f"{message_not_updated}"})


class ListUserOrders(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Get all user's orders",
        operation_description="This API endpoint allows"
                              " user to get all the orders of the user"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class ClearUserOrders(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Clear orders history",
        operation_description="This API endpoint allows"
                              " user to clear user's order history"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def delete(self, request, *args, **kwargs):
        objects = Order.objects.filter(user=request.user)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListUserListedBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = UserListedBooksSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    @swagger_auto_schema(
        name="Get all user's listed books",
        operation_description="This API endpoint allows"
                              "user to get all the books which the user listed"
                              ".[only if an user is authenticated]",
        tags=["Profile"],
    )
    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(author=request.user)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
