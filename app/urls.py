from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path("seller/", views.seller, name="seller"),
    path("seller_payment/", views.seller_payment, name="seller_payment"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path("electronic_search/", views.electronic_search, name="electronic_search"),
    path("shoes_list/", views.shoes_list, name="shoes_list"),
    path("cloth_list/", views.cloth_list, name="cloth_list"),
    path("searchbyprice_range/", views.searchbyprice_range, name="searchbyprice_range"),
    path("sortingbyprice/", views.sortingbyprice, name="sortingbyprice"),
    path(
        "productdetails/<int:productid>/", views.productdetails, name="productdetails"
    ),
    path("show_wishlist/", views.show_wishlist, name="show_wishlist"),
    path("addtowishlist/<int:productid>/", views.addtowishlist, name="addtowishlist"),
    path(
        "removewishlist/<int:productid>/", views.removewishlist, name="removewishlist"
    ),
    path("showcarts/", views.showcarts, name="showcarts"),
    path("updateqty/<int:qv>/<int:productid>/", views.updateqty, name="updateqty"),
    path("addtocart/<int:productid>/", views.addtocart, name="addtocart"),
    path(
        "removefromcart/<int:productid>/", views.removefromcart, name="removefromcart"
    ),
    path("myprofile/", views.myprofile, name="myprofile"),
    path("addprofile/", views.addprofile, name="addprofile"),
    path("editprofile/<int:profileid>/", views.editprofile, name="editprofile"),
    path("addaddress/", views.addaddress, name="addaddress"),
    path("editaddress/<int:addressid>/", views.editaddress, name="editaddress"),
    path("deleteaddress/<int:addressid>/", views.deleteaddress, name="deleteaddress"),
    path("checkout/", views.checkout, name="checkout"),
    path('checkoutsingle/<int:productid>/',views.checkoutsingle,name='checkoutsingle'),
    path('placeorder/',views.placeorder,name="placeorder"),
    path('payment_success/',views.payment_success,name='payment_success'),
    path('payment/',views.payment,name='payment'),
]
