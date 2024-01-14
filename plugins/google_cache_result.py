from urllib.parse import urlparse
from osintbuddy.elements import Title, CopyText
from osintbuddy import transform, DiscoverableEntity, EntityRegistry


class GoogleCacheResult(DiscoverableEntity):
    label = "Google Cache Result"
    icon = "brand-google-filled"
    color = "#145070"
    show_label = False

    properties = [
        Title(label="result", title="Some title"),
        [CopyText(label="URL")],
    ]

    author = "Team@ICG"
    description = ""

    @transform(label="To website", icon="world-www")
    async def transform_to_website(self, node, use):
        WebsitePlugin = await EntityRegistry.get_plugin('website')
        return WebsitePlugin.create(domain=urlparse(node.url).netloc)
