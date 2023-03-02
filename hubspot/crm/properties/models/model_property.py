# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.properties.configuration import Configuration


class ModelProperty(object):
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
    openapi_types = {
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'archived_at': 'datetime',
        'name': 'str',
        'label': 'str',
        'type': 'str',
        'field_type': 'str',
        'description': 'str',
        'group_name': 'str',
        'options': 'list[Option]',
        'created_user_id': 'str',
        'updated_user_id': 'str',
        'referenced_object_type': 'str',
        'display_order': 'int',
        'calculated': 'bool',
        'external_options': 'bool',
        'archived': 'bool',
        'has_unique_value': 'bool',
        'hidden': 'bool',
        'hubspot_defined': 'bool',
        'show_currency_symbol': 'bool',
        'modification_metadata': 'PropertyModificationMetadata',
        'form_field': 'bool',
        'calculation_formula': 'str'
    }

    attribute_map = {
        'updated_at': 'updatedAt',
        'created_at': 'createdAt',
        'archived_at': 'archivedAt',
        'name': 'name',
        'label': 'label',
        'type': 'type',
        'field_type': 'fieldType',
        'description': 'description',
        'group_name': 'groupName',
        'options': 'options',
        'created_user_id': 'createdUserId',
        'updated_user_id': 'updatedUserId',
        'referenced_object_type': 'referencedObjectType',
        'display_order': 'displayOrder',
        'calculated': 'calculated',
        'external_options': 'externalOptions',
        'archived': 'archived',
        'has_unique_value': 'hasUniqueValue',
        'hidden': 'hidden',
        'hubspot_defined': 'hubspotDefined',
        'show_currency_symbol': 'showCurrencySymbol',
        'modification_metadata': 'modificationMetadata',
        'form_field': 'formField',
        'calculation_formula': 'calculationFormula'
    }

    def __init__(self, updated_at=None, created_at=None, archived_at=None, name=None, label=None, type=None, field_type=None, description=None, group_name=None, options=None, created_user_id=None, updated_user_id=None, referenced_object_type=None, display_order=None, calculated=None, external_options=None, archived=None, has_unique_value=None, hidden=None, hubspot_defined=None, show_currency_symbol=None, modification_metadata=None, form_field=None, calculation_formula=None, local_vars_configuration=None):  # noqa: E501
        """ModelProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._updated_at = None
        self._created_at = None
        self._archived_at = None
        self._name = None
        self._label = None
        self._type = None
        self._field_type = None
        self._description = None
        self._group_name = None
        self._options = None
        self._created_user_id = None
        self._updated_user_id = None
        self._referenced_object_type = None
        self._display_order = None
        self._calculated = None
        self._external_options = None
        self._archived = None
        self._has_unique_value = None
        self._hidden = None
        self._hubspot_defined = None
        self._show_currency_symbol = None
        self._modification_metadata = None
        self._form_field = None
        self._calculation_formula = None
        self.discriminator = None

        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at
        if archived_at is not None:
            self.archived_at = archived_at
        self.name = name
        self.label = label
        self.type = type
        self.field_type = field_type
        self.description = description
        self.group_name = group_name
        self.options = options
        if created_user_id is not None:
            self.created_user_id = created_user_id
        if updated_user_id is not None:
            self.updated_user_id = updated_user_id
        if referenced_object_type is not None:
            self.referenced_object_type = referenced_object_type
        if display_order is not None:
            self.display_order = display_order
        if calculated is not None:
            self.calculated = calculated
        if external_options is not None:
            self.external_options = external_options
        if archived is not None:
            self.archived = archived
        if has_unique_value is not None:
            self.has_unique_value = has_unique_value
        if hidden is not None:
            self.hidden = hidden
        if hubspot_defined is not None:
            self.hubspot_defined = hubspot_defined
        if show_currency_symbol is not None:
            self.show_currency_symbol = show_currency_symbol
        if modification_metadata is not None:
            self.modification_metadata = modification_metadata
        if form_field is not None:
            self.form_field = form_field
        if calculation_formula is not None:
            self.calculation_formula = calculation_formula

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelProperty.  # noqa: E501


        :return: The updated_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelProperty.


        :param updated_at: The updated_at of this ModelProperty.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ModelProperty.  # noqa: E501


        :return: The created_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelProperty.


        :param created_at: The created_at of this ModelProperty.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def archived_at(self):
        """Gets the archived_at of this ModelProperty.  # noqa: E501

        When the property was archived.  # noqa: E501

        :return: The archived_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this ModelProperty.

        When the property was archived.  # noqa: E501

        :param archived_at: The archived_at of this ModelProperty.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def name(self):
        """Gets the name of this ModelProperty.  # noqa: E501

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :return: The name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelProperty.

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :param name: The name of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this ModelProperty.  # noqa: E501

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelProperty.

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def type(self):
        """Gets the type of this ModelProperty.  # noqa: E501

        The property data type.  # noqa: E501

        :return: The type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelProperty.

        The property data type.  # noqa: E501

        :param type: The type of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def field_type(self):
        """Gets the field_type of this ModelProperty.  # noqa: E501

        Controls how the property appears in HubSpot.  # noqa: E501

        :return: The field_type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this ModelProperty.

        Controls how the property appears in HubSpot.  # noqa: E501

        :param field_type: The field_type of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def description(self):
        """Gets the description of this ModelProperty.  # noqa: E501

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :return: The description of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelProperty.

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :param description: The description of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def group_name(self):
        """Gets the group_name of this ModelProperty.  # noqa: E501

        The name of the property group the property belongs to.  # noqa: E501

        :return: The group_name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ModelProperty.

        The name of the property group the property belongs to.  # noqa: E501

        :param group_name: The group_name of this ModelProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def options(self):
        """Gets the options of this ModelProperty.  # noqa: E501

        A list of valid options for the property. This field is required for enumerated properties, but will be empty for other property types.  # noqa: E501

        :return: The options of this ModelProperty.  # noqa: E501
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ModelProperty.

        A list of valid options for the property. This field is required for enumerated properties, but will be empty for other property types.  # noqa: E501

        :param options: The options of this ModelProperty.  # noqa: E501
        :type: list[Option]
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def created_user_id(self):
        """Gets the created_user_id of this ModelProperty.  # noqa: E501

        The internal user ID of the user who created the property in HubSpot. This field may not exist if the property was created outside of HubSpot.  # noqa: E501

        :return: The created_user_id of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        """Sets the created_user_id of this ModelProperty.

        The internal user ID of the user who created the property in HubSpot. This field may not exist if the property was created outside of HubSpot.  # noqa: E501

        :param created_user_id: The created_user_id of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._created_user_id = created_user_id

    @property
    def updated_user_id(self):
        """Gets the updated_user_id of this ModelProperty.  # noqa: E501

        The internal user ID of the user who updated the property in HubSpot. This field may not exist if the property was updated outside of HubSpot.  # noqa: E501

        :return: The updated_user_id of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._updated_user_id

    @updated_user_id.setter
    def updated_user_id(self, updated_user_id):
        """Sets the updated_user_id of this ModelProperty.

        The internal user ID of the user who updated the property in HubSpot. This field may not exist if the property was updated outside of HubSpot.  # noqa: E501

        :param updated_user_id: The updated_user_id of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._updated_user_id = updated_user_id

    @property
    def referenced_object_type(self):
        """Gets the referenced_object_type of this ModelProperty.  # noqa: E501

        If this property is related to other object(s), they'll be listed here.  # noqa: E501

        :return: The referenced_object_type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._referenced_object_type

    @referenced_object_type.setter
    def referenced_object_type(self, referenced_object_type):
        """Sets the referenced_object_type of this ModelProperty.

        If this property is related to other object(s), they'll be listed here.  # noqa: E501

        :param referenced_object_type: The referenced_object_type of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._referenced_object_type = referenced_object_type

    @property
    def display_order(self):
        """Gets the display_order of this ModelProperty.  # noqa: E501

        Properties are shown in order, starting with the lowest positive integer value.  # noqa: E501

        :return: The display_order of this ModelProperty.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this ModelProperty.

        Properties are shown in order, starting with the lowest positive integer value.  # noqa: E501

        :param display_order: The display_order of this ModelProperty.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def calculated(self):
        """Gets the calculated of this ModelProperty.  # noqa: E501

        For default properties, true indicates that the property is calculated by a HubSpot process. It has no effect for custom properties.  # noqa: E501

        :return: The calculated of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._calculated

    @calculated.setter
    def calculated(self, calculated):
        """Sets the calculated of this ModelProperty.

        For default properties, true indicates that the property is calculated by a HubSpot process. It has no effect for custom properties.  # noqa: E501

        :param calculated: The calculated of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._calculated = calculated

    @property
    def external_options(self):
        """Gets the external_options of this ModelProperty.  # noqa: E501

        For default properties, true indicates that the options are stored externally to the property settings.  # noqa: E501

        :return: The external_options of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._external_options

    @external_options.setter
    def external_options(self, external_options):
        """Sets the external_options of this ModelProperty.

        For default properties, true indicates that the options are stored externally to the property settings.  # noqa: E501

        :param external_options: The external_options of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._external_options = external_options

    @property
    def archived(self):
        """Gets the archived of this ModelProperty.  # noqa: E501

        Whether or not the property is archived.  # noqa: E501

        :return: The archived of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ModelProperty.

        Whether or not the property is archived.  # noqa: E501

        :param archived: The archived of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def has_unique_value(self):
        """Gets the has_unique_value of this ModelProperty.  # noqa: E501

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :return: The has_unique_value of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._has_unique_value

    @has_unique_value.setter
    def has_unique_value(self, has_unique_value):
        """Sets the has_unique_value of this ModelProperty.

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :param has_unique_value: The has_unique_value of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._has_unique_value = has_unique_value

    @property
    def hidden(self):
        """Gets the hidden of this ModelProperty.  # noqa: E501

        Whether or not the property will be hidden from the HubSpot UI. It's recommended this be set to false for custom properties.  # noqa: E501

        :return: The hidden of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ModelProperty.

        Whether or not the property will be hidden from the HubSpot UI. It's recommended this be set to false for custom properties.  # noqa: E501

        :param hidden: The hidden of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def hubspot_defined(self):
        """Gets the hubspot_defined of this ModelProperty.  # noqa: E501

        This will be true for default object properties built into HubSpot.  # noqa: E501

        :return: The hubspot_defined of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._hubspot_defined

    @hubspot_defined.setter
    def hubspot_defined(self, hubspot_defined):
        """Sets the hubspot_defined of this ModelProperty.

        This will be true for default object properties built into HubSpot.  # noqa: E501

        :param hubspot_defined: The hubspot_defined of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._hubspot_defined = hubspot_defined

    @property
    def show_currency_symbol(self):
        """Gets the show_currency_symbol of this ModelProperty.  # noqa: E501

        Whether or not the property will display the currency symbol set in the account settings.  # noqa: E501

        :return: The show_currency_symbol of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._show_currency_symbol

    @show_currency_symbol.setter
    def show_currency_symbol(self, show_currency_symbol):
        """Sets the show_currency_symbol of this ModelProperty.

        Whether or not the property will display the currency symbol set in the account settings.  # noqa: E501

        :param show_currency_symbol: The show_currency_symbol of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._show_currency_symbol = show_currency_symbol

    @property
    def modification_metadata(self):
        """Gets the modification_metadata of this ModelProperty.  # noqa: E501


        :return: The modification_metadata of this ModelProperty.  # noqa: E501
        :rtype: PropertyModificationMetadata
        """
        return self._modification_metadata

    @modification_metadata.setter
    def modification_metadata(self, modification_metadata):
        """Sets the modification_metadata of this ModelProperty.


        :param modification_metadata: The modification_metadata of this ModelProperty.  # noqa: E501
        :type: PropertyModificationMetadata
        """

        self._modification_metadata = modification_metadata

    @property
    def form_field(self):
        """Gets the form_field of this ModelProperty.  # noqa: E501

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :return: The form_field of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._form_field

    @form_field.setter
    def form_field(self, form_field):
        """Sets the form_field of this ModelProperty.

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :param form_field: The form_field of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._form_field = form_field

    @property
    def calculation_formula(self):
        """Gets the calculation_formula of this ModelProperty.  # noqa: E501

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :return: The calculation_formula of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._calculation_formula

    @calculation_formula.setter
    def calculation_formula(self, calculation_formula):
        """Sets the calculation_formula of this ModelProperty.

        Represents a formula that is used to compute a calculated property.  # noqa: E501

        :param calculation_formula: The calculation_formula of this ModelProperty.  # noqa: E501
        :type: str
        """

        self._calculation_formula = calculation_formula

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProperty):
            return True

        return self.to_dict() != other.to_dict()
