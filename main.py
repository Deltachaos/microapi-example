from app.config import service_providers
from microapi.bridge.cloudflare import App

app = App(service_providers=service_providers())
on_fetch = app.on_fetch()
on_scheduled = app.on_scheduled()