# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.contacts.configuration import Configuration


class PublicGdprDeleteInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"id_property": "str", "object_id": "str"}

    attribute_map = {"id_property": "idProperty", "object_id": "objectId"}

    def __init__(self, id_property=None, object_id=None, local_vars_configuration=None):  # noqa: E501
        """PublicGdprDeleteInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id_property = None
        self._object_id = None
        self.discriminator = None

        if id_property is not None:
            self.id_property = id_property
        self.object_id = object_id

    @property
    def id_property(self):
        """Gets the id_property of this PublicGdprDeleteInput.  # noqa: E501


        :return: The id_property of this PublicGdprDeleteInput.  # noqa: E501
        :rtype: str
        """
        return self._id_property

    @id_property.setter
    def id_property(self, id_property):
        """Sets the id_property of this PublicGdprDeleteInput.


        :param id_property: The id_property of this PublicGdprDeleteInput.  # noqa: E501
        :type id_property: str
        """

        self._id_property = id_property

    @property
    def object_id(self):
        """Gets the object_id of this PublicGdprDeleteInput.  # noqa: E501


        :return: The object_id of this PublicGdprDeleteInput.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this PublicGdprDeleteInput.


        :param object_id: The object_id of this PublicGdprDeleteInput.  # noqa: E501
        :type object_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicGdprDeleteInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicGdprDeleteInput):
            return True

        return self.to_dict() != other.to_dict()
