from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet, VendorViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet,
    CartViewSet, CartItemViewSet, ShippingViewSet, PaymentViewSet, CouponViewSet, ReviewViewSet,
    WishlistViewSet, NotificationViewSet, BlogViewSet, ContactViewSet, FAQViewSet, 
    AnalyticsViewSet, ConfigurationViewSet, TaxViewSet, SubscriptionViewSet, RefundViewSet
)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('vendors', VendorViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('carts', CartViewSet)
router.register('cart-items', CartItemViewSet)
router.register('shipping', ShippingViewSet)
router.register('payments', PaymentViewSet)
router.register('coupons', CouponViewSet)
router.register('reviews', ReviewViewSet)
router.register('wishlist', WishlistViewSet)
router.register('notifications', NotificationViewSet)
router.register('blogs', BlogViewSet)
router.register('contacts', ContactViewSet)
router.register('faqs', FAQViewSet)
router.register('analytics', AnalyticsViewSet)
router.register('configurations', ConfigurationViewSet)
router.register('taxes', TaxViewSet)
router.register('subscriptions', SubscriptionViewSet)
router.register('refunds', RefundViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
]
