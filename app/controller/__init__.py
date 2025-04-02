from microapi.di import tag
from microapi.bridge.cloudflare import CloudContext as CloudflareCloudContext
from microapi.bridge.cloudflare.util import to_py
from microapi.http import Response
from microapi.router import route

@tag('controller')
class MyController:
    def __init__(self, context: CloudflareCloudContext):
        self.context = context

    @route('/some/{data}')
    async def action(self, data: str):
        store = await self.context.binding("SOME_KV_STORE")
        store_data = to_py(await store.get(data))
        return Response(f"data {store_data}")