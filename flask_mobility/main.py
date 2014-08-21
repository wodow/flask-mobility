
from flask import _request_ctx_stack as stack

from user_agents import parse as parse_user_agent


class Mobility(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app

        @app.before_request
        def before_request():
            ctx = stack.top
            if ctx is not None and hasattr(ctx, 'request'):
                self.process_request(ctx.request)

    def process_request(self, request):
        ua_str = request.user_agent.string.lower()

        user_agent = parse_user_agent(ua_str)

        request.DESKTOP = user_agent.is_pc
        request.MOBILE = user_agent.is_mobile
        request.TABLET = user_agent.is_tablet
        request.TOUCH_CAPABLE = user_agent.is_touch_capable
        request.BOT = user_agent.is_bot
