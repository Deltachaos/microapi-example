from app.controller import MyController
from microapi.config import FrameworkServiceProvider
from microapi.di import ServiceProvider

class AppServiceProvider(ServiceProvider):
    def services(self):
        yield MyController


def service_providers():
    yield FrameworkServiceProvider()
    yield AppServiceProvider()