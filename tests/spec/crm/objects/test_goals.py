from hubspot import HubSpot
from hubspot.crm.objects.goals import BasicApi, BatchApi, SearchApi


def test_is_discoverable():
    apis = HubSpot().crm.objects.goals
    assert isinstance(apis.basic_api, BasicApi)
    assert isinstance(apis.batch_api, BatchApi)
    assert isinstance(apis.search_api, SearchApi)