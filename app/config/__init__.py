from app.controller import MyController
from app.event_subscriber import MyEventSubscriber
from microapi.config import FrameworkServiceProvider
from microapi.di import ServiceProvider

class AppServiceProvider(ServiceProvider):
    def services(self):
        yield MyController
        yield MyEventSubscriber


def service_providers():
    yield FrameworkServiceProvider()
    yield AppServiceProvider()