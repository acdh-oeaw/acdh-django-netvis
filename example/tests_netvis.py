from django.test import TestCase
from django.urls import reverse
from example.models import Place


class NetVisTestCase(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        self.place_name = 'Linz'
        self.place = Place.objects.get(name=self.place_name)
        self.qs_place_url = reverse(
            'netvis:qs_as_graph',
            kwargs={
                'app_name': 'example',
                'model_name': 'place'
            }
        )
        self.node_url = reverse(
            'netvis:graph',
            kwargs={
                'app_name': 'example',
                'model_name': 'place',
                'pk': self.place.id
            }
        )

    def test_001_graph_qs_endpoint(self):
        r = self.client.get(self.qs_place_url)
        self.assertEqual(r.status_code, 200)
    
    def test_002_graph_qs_endpoint_keys(self):
        r = self.client.get(self.qs_place_url)
        graph = r.json()
        self.assertTrue('edges' in graph.keys())
        self.assertTrue('nodes' in graph.keys())
        self.assertFalse('hansi4ever' in graph.keys())
    
    def test_003_node_endpoint(self):
        r = self.client.get(self.node_url)
        self.assertEqual(r.status_code, 200)
        graph = r.json()
        node_label = graph['nodes'][0]['label']
        self.assertEqual(node_label, self.place_name)