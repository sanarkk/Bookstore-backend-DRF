from django.urls import path
from .views import (
    ListBooksAPI,
    CreateBookAPI,
    UpdateBookAPI,
    RetrieveBookAPI,
    CreateOrderAPI,
    GetOrderAPI,
    ListUserInformation,
    UpdateUserInformation,
    ListUserOrders,
    ClearUserOrders,
)

urlpatterns = [
    path("get_book_list/", ListBooksAPI.as_view()),
    path("create_book/", CreateBookAPI.as_view()),
    path("update_book/<int:pk>", UpdateBookAPI.as_view()),
    path("get_book/<int:pk>", RetrieveBookAPI.as_view()),
    path("create_order/", CreateOrderAPI.as_view()),
    path("get_order/<int:pk>", GetOrderAPI.as_view()),
    path("profile/", ListUserInformation.as_view()),
    path("update_profile/", UpdateUserInformation.as_view()),
    path("orders/", ListUserOrders.as_view()),
    path("clear_orders/", ClearUserOrders.as_view()),
]
