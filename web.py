import os
from keeper_secrets_manager_core import SecretsManager
from keeper_secrets_manager_core.storage import FileKeyValueStorage
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')


def make_app():
    
    try:
        token = os.environ["KSM_TOKEN"]
    except:
        raise RuntimeError("KSM token needs to be passed as KSM_TOKEN environment variable")
    secrets_manager = SecretsManager(
        token=token,
        config=FileKeyValueStorage('ksm-config.json')
    )

    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    return app

wsgi = make_app()
