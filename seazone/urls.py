from rest_framework import routers
from core.views.agenda import AgendaModelViewSet
from core.views.host import HostModelViewSet
from core.views.schedule import ScheduleModelViewSet
from core.views.superstructure import SuperstructureModelViewSet
from django.urls import path


router = routers.SimpleRouter()

router.register(r'agendas', AgendaModelViewSet, basename='agenda')
router.register(r'hosts', HostModelViewSet, basename='host')
router.register(r'schedules', ScheduleModelViewSet, basename='schedule')
router.register(r'superstructures', SuperstructureModelViewSet, basename='superstructure')

all_agendas = HostModelViewSet.as_view({
    'get': 'get_agenda',
})

urlpatterns = [
    path('host/<int:host_id>/agenda', all_agendas),
]

urlpatterns += router.urls
