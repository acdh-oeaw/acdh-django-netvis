import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


from netvis.models import NetVisCache
from netvis.utils import qs_as_graph


class Command(BaseCommand):

    help = "Populate the netvis cache"

    def add_arguments(self, parser):
        parser.add_argument(
            'app_name', type=str,
            help="Name of the app for which you'd like to populate the cache."
        )
        parser.add_argument(
            'model_name', type=str,
            help="Name of the model for which  you'd like to populate the cache."
        )

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        model_name = kwargs['model_name']
        try:
            ct = ContentType.objects.get(app_label=app_name, model=model_name)
        except ObjectDoesNotExist:
            return f"A model: {model_name} in app: {app_name} could not be found"
        qs = ct.model_class().objects.all()
        limit = len(qs)
        graph = qs_as_graph(qs, limit=limit)
        netvis_cache, _ = NetVisCache.objects.get_or_create(
            app_name=app_name,
            model_name=model_name
        )
        graph_prev = qs_as_graph(qs)
        netvis_cache.graph_data = json.dumps(graph)
        netvis_cache.graph_data_preview = json.dumps(graph_prev)
        netvis_cache.save()
        return "done"
