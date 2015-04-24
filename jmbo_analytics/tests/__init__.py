from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django import template


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

    def test_google_analytics_tag(self):
        setattr(self.request, "GET", {})
        setattr(self.request, "META", {"HTTP_REFERER": "/from/page/"})
        setattr(self.request, "path", "/some/page/")
        self.context = template.Context({"request": self.request})
        t = template.Template(
            "{% load jmbo_analytics_tags %}{% google_analytics %}"
        )
        self.failUnlessEqual(
            t.render(self.context),
            "/google-analytics/?p=%2Fsome%2Fpage%2F&r=%2Ffrom%2Fpage%2F"
        )
