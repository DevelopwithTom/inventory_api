from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')  

urlpatterns = router.urls