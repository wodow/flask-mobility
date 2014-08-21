import unittest

from flask import Flask, render_template_string
from flask.ext.mobility import Mobility

from constants import ANDROID_BROWSER_UA


class MobilityTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        Mobility(app)

        @app.route('/')
        def index():
            tpl = '{% if request.MOBILE %}True{% else %}False{% endif %}'
            return render_template_string(tpl)

        self.app = app.test_client()
        self.config = app.config

    def test_detect_mobile_user_agent(self):
        """Check that mobile user agents are properly detected"""

        # Check without mobile User-Agent header
        assert b'False' == self.app.get('/').data

        # Check with mobile User-Agent header
        headers = [('User-Agent', ANDROID_BROWSER_UA)]
        assert b'True' == self.app.get('/', headers=headers).data
