import unittest

from flask import Flask, render_template_string
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template, mobilized

from constants import ANDROID_BROWSER_UA


class DecoratorsTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route('/')
        @mobile_template('{mobile/}template.html')
        def index(template):
            return render_template_string(template)

        # Default View
        def mobilize():
            return render_template_string('False')

        # Mobilized view
        @app.route('/mobilize')
        @mobilized(mobilize)
        def mobilize():
            return render_template_string('True')

        self.app = app
        self.client = app.test_client()

    def test_mobile_template_user_agent(self):
        """Test the mobile_template decorator"""

        # Check without mobile User-Agent header
        assert b'template.html' == self.client.get('/').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', ANDROID_BROWSER_UA)]
        response = self.client.get('/', headers=headers)
        assert b'mobile/template.html' == response.data

    def test_mobilized_user_agent(self):
        """Test the mobilized decorator"""

        # Check without mobile User-Agent header
        assert b'False' == self.client.get('/mobilize').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', ANDROID_BROWSER_UA)]
        assert b'True' == self.client.get('/mobilize', headers=headers).data
