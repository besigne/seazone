from rest_framework import routers
from core.views.agenda import AgendaModelViewSet
from core.views.host import HostModelViewSet
from core.views.event import EventModelViewSet
from core.views.superstructure import SuperstructureModelViewSet

router = routers.SimpleRouter()

router.register(r'agendas', AgendaModelViewSet, basename='agenda')
router.register(r'hosts', HostModelViewSet, basename='host')
router.register(r'events', EventModelViewSet, basename='event')
router.register(r'superstructures', SuperstructureModelViewSet, basename='superstructure')


urlpatterns = router.urls
