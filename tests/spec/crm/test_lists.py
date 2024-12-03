from hubspot import HubSpot
from hubspot.crm.lists import FoldersApi, ListsApi, MappingApi, MembershipsApi


def test_is_discoverable():
    apis = HubSpot().crm.lists
    assert isinstance(apis.folders_api, FoldersApi)
    assert isinstance(apis.lists_api, ListsApi)
    assert isinstance(apis.mapping_api, MappingApi)
    assert isinstance(apis.memberships_api, MembershipsApi)