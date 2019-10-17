# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ARMErrorResponseBody(Model):
    """ARM error response body.

    :param message: Gets or sets the string that describes the error in detail
     and provides debugging information.
    :type message: str
    :param code: Gets or sets the string that can be used to programmatically
     identify the error.
    :type code: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(self, *, message: str=None, code: str=None, **kwargs) -> None:
        super(ARMErrorResponseBody, self).__init__(**kwargs)
        self.message = message
        self.code = code


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ConfigData(Model):
    """The Advisor configuration data structure.

    :param id: The resource Id of the configuration resource.
    :type id: str
    :param type: The type of the configuration resource.
    :type type: str
    :param name: The name of the configuration resource.
    :type name: str
    :param properties: The list of property name/value pairs.
    :type properties: ~azure.mgmt.advisor.models.ConfigDataProperties
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfigDataProperties'},
    }

    def __init__(self, *, id: str=None, type: str=None, name: str=None, properties=None, **kwargs) -> None:
        super(ConfigData, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.properties = properties


class ConfigDataProperties(Model):
    """The list of property name/value pairs.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param exclude: Exclude the resource from Advisor evaluations. Valid
     values: False (default) or True.
    :type exclude: bool
    :param low_cpu_threshold: Minimum percentage threshold for Advisor low CPU
     utilization evaluation. Valid only for subscriptions. Valid values: 5
     (default), 10, 15 or 20.
    :type low_cpu_threshold: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'exclude': {'key': 'exclude', 'type': 'bool'},
        'low_cpu_threshold': {'key': 'low_cpu_threshold', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, exclude: bool=None, low_cpu_threshold: str=None, **kwargs) -> None:
        super(ConfigDataProperties, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.exclude = exclude
        self.low_cpu_threshold = low_cpu_threshold


class MetadataEntity(Model):
    """The metadata entity contract.

    :param id: The resource Id of the metadata entity.
    :type id: str
    :param type: The type of the metadata entity.
    :type type: str
    :param name: The name of the metadata entity.
    :type name: str
    :param display_name: The display name.
    :type display_name: str
    :param depends_on: The list of keys on which this entity depends on.
    :type depends_on: list[str]
    :param applicable_scenarios: The list of scenarios applicable to this
     metadata entity.
    :type applicable_scenarios: list[str or
     ~azure.mgmt.advisor.models.Scenario]
    :param supported_values: The list of supported values.
    :type supported_values:
     list[~azure.mgmt.advisor.models.MetadataSupportedValueDetail]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'depends_on': {'key': 'properties.dependsOn', 'type': '[str]'},
        'applicable_scenarios': {'key': 'properties.applicableScenarios', 'type': '[str]'},
        'supported_values': {'key': 'properties.supportedValues', 'type': '[MetadataSupportedValueDetail]'},
    }

    def __init__(self, *, id: str=None, type: str=None, name: str=None, display_name: str=None, depends_on=None, applicable_scenarios=None, supported_values=None, **kwargs) -> None:
        super(MetadataEntity, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.display_name = display_name
        self.depends_on = depends_on
        self.applicable_scenarios = applicable_scenarios
        self.supported_values = supported_values


class MetadataSupportedValueDetail(Model):
    """The metadata supported value detail.

    :param id: The id.
    :type id: str
    :param display_name: The display name.
    :type display_name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, display_name: str=None, **kwargs) -> None:
        super(MetadataSupportedValueDetail, self).__init__(**kwargs)
        self.id = id
        self.display_name = display_name


class OperationDisplayInfo(Model):
    """The operation supported by Advisor.

    :param description: The description of the operation.
    :type description: str
    :param operation: The action that users can perform, based on their
     permission level.
    :type operation: str
    :param provider: Service provider: Microsoft Advisor.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, operation: str=None, provider: str=None, resource: str=None, **kwargs) -> None:
        super(OperationDisplayInfo, self).__init__(**kwargs)
        self.description = description
        self.operation = operation
        self.provider = provider
        self.resource = resource


class OperationEntity(Model):
    """The operation supported by Advisor.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The operation supported by Advisor.
    :type display: ~azure.mgmt.advisor.models.OperationDisplayInfo
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayInfo'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(OperationEntity, self).__init__(**kwargs)
        self.name = name
        self.display = display


class Resource(Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ResourceRecommendationBase(Resource):
    """Advisor Recommendation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param category: The category of the recommendation. Possible values
     include: 'HighAvailability', 'Security', 'Performance', 'Cost',
     'OperationalExcellence'
    :type category: str or ~azure.mgmt.advisor.models.Category
    :param impact: The business impact of the recommendation. Possible values
     include: 'High', 'Medium', 'Low'
    :type impact: str or ~azure.mgmt.advisor.models.Impact
    :param impacted_field: The resource type identified by Advisor.
    :type impacted_field: str
    :param impacted_value: The resource identified by Advisor.
    :type impacted_value: str
    :param last_updated: The most recent time that Advisor checked the
     validity of the recommendation.
    :type last_updated: datetime
    :param metadata: The recommendation metadata.
    :type metadata: dict[str, object]
    :param recommendation_type_id: The recommendation-type GUID.
    :type recommendation_type_id: str
    :param risk: The potential risk of not implementing the recommendation.
     Possible values include: 'Error', 'Warning', 'None'
    :type risk: str or ~azure.mgmt.advisor.models.Risk
    :param short_description: A summary of the recommendation.
    :type short_description: ~azure.mgmt.advisor.models.ShortDescription
    :param suppression_ids: The list of snoozed and dismissed rules for the
     recommendation.
    :type suppression_ids: list[str]
    :param extended_properties: Extended properties
    :type extended_properties: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'impact': {'key': 'properties.impact', 'type': 'str'},
        'impacted_field': {'key': 'properties.impactedField', 'type': 'str'},
        'impacted_value': {'key': 'properties.impactedValue', 'type': 'str'},
        'last_updated': {'key': 'properties.lastUpdated', 'type': 'iso-8601'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
        'recommendation_type_id': {'key': 'properties.recommendationTypeId', 'type': 'str'},
        'risk': {'key': 'properties.risk', 'type': 'str'},
        'short_description': {'key': 'properties.shortDescription', 'type': 'ShortDescription'},
        'suppression_ids': {'key': 'properties.suppressionIds', 'type': '[str]'},
        'extended_properties': {'key': 'properties.extendedProperties', 'type': '{str}'},
    }

    def __init__(self, *, category=None, impact=None, impacted_field: str=None, impacted_value: str=None, last_updated=None, metadata=None, recommendation_type_id: str=None, risk=None, short_description=None, suppression_ids=None, extended_properties=None, **kwargs) -> None:
        super(ResourceRecommendationBase, self).__init__(**kwargs)
        self.category = category
        self.impact = impact
        self.impacted_field = impacted_field
        self.impacted_value = impacted_value
        self.last_updated = last_updated
        self.metadata = metadata
        self.recommendation_type_id = recommendation_type_id
        self.risk = risk
        self.short_description = short_description
        self.suppression_ids = suppression_ids
        self.extended_properties = extended_properties


class ShortDescription(Model):
    """A summary of the recommendation.

    :param problem: The issue or opportunity identified by the recommendation.
    :type problem: str
    :param solution: The remediation action suggested by the recommendation.
    :type solution: str
    """

    _attribute_map = {
        'problem': {'key': 'problem', 'type': 'str'},
        'solution': {'key': 'solution', 'type': 'str'},
    }

    def __init__(self, *, problem: str=None, solution: str=None, **kwargs) -> None:
        super(ShortDescription, self).__init__(**kwargs)
        self.problem = problem
        self.solution = solution


class SuppressionContract(Resource):
    """The details of the snoozed or dismissed rule; for example, the duration,
    name, and GUID associated with the rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param suppression_id: The GUID of the suppression.
    :type suppression_id: str
    :param ttl: The duration for which the suppression is valid.
    :type ttl: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'suppression_id': {'key': 'properties.suppressionId', 'type': 'str'},
        'ttl': {'key': 'properties.ttl', 'type': 'str'},
    }

    def __init__(self, *, suppression_id: str=None, ttl: str=None, **kwargs) -> None:
        super(SuppressionContract, self).__init__(**kwargs)
        self.suppression_id = suppression_id
        self.ttl = ttl
