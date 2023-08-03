# coding: utf-8

# flake8: noqa
"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from hubspot.webhooks.models.batch_input_subscription_batch_update_request import BatchInputSubscriptionBatchUpdateRequest
from hubspot.webhooks.models.batch_response_subscription_response import BatchResponseSubscriptionResponse
from hubspot.webhooks.models.batch_response_subscription_response_with_errors import BatchResponseSubscriptionResponseWithErrors
from hubspot.webhooks.models.error import Error
from hubspot.webhooks.models.error_detail import ErrorDetail
from hubspot.webhooks.models.settings_change_request import SettingsChangeRequest
from hubspot.webhooks.models.settings_response import SettingsResponse
from hubspot.webhooks.models.standard_error import StandardError
from hubspot.webhooks.models.subscription_batch_update_request import SubscriptionBatchUpdateRequest
from hubspot.webhooks.models.subscription_create_request import SubscriptionCreateRequest
from hubspot.webhooks.models.subscription_list_response import SubscriptionListResponse
from hubspot.webhooks.models.subscription_patch_request import SubscriptionPatchRequest
from hubspot.webhooks.models.subscription_response import SubscriptionResponse
from hubspot.webhooks.models.throttling_settings import ThrottlingSettings
