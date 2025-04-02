from microapi.bridge import CloudContext
from microapi.bridge.cloudflare import CloudContext as CloudflareCloudContext
from microapi.bridge.cloudflare.util import to_py
from microapi.http import JsonResponse
from microapi.kernel import ViewEvent
from microapi.cron import CronEvent
from microapi.di import tag
from microapi.event import listen
from microapi.kernel import RequestEvent
from microapi.util import logger

@tag('event_subscriber')
class MyEventSubscriber:
    def __init__(self, context: CloudContext):
        self.context = context

    @listen(RequestEvent)
    def some_event(self, event: RequestEvent):
        logger(__name__).debug(f"Received {event.request.body()}")

    @listen(ViewEvent)
    def some_event(self, event: ViewEvent):
        event.response = JsonResponse(event.controller_result, status_code=400, headers={"X-Some-Header": "value"})

    @listen(CronEvent)
    async def on_cron(self, event: CronEvent):
        if isinstance(self.context, CloudflareCloudContext):
            store = await self.context.binding("SOME_KV_STORE")
            store_data = to_py(await store.get("some_key"))
            logger(__name__).info(f"Cron event {store_data}")