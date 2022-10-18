from rest_framework.routers import SimpleRouter


from .views import LedgerViewSet

router = SimpleRouter()
router.register("", LedgerViewSet, basename="ledgers")

urlpatterns = router.urls