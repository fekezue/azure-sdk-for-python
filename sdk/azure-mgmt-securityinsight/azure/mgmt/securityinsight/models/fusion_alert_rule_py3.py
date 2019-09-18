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

from .alert_rule_py3 import AlertRule


class FusionAlertRule(AlertRule):
    """Represents Fusion alert rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param etag: Etag of the azure resource
    :type etag: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param alert_rule_template_name: Required. The Name of the alert rule
     template used to create this rule.
    :type alert_rule_template_name: str
    :ivar description: The description of the alert rule.
    :vartype description: str
    :ivar display_name: The display name for alerts created by this alert
     rule.
    :vartype display_name: str
    :param enabled: Required. Determines whether this alert rule is enabled or
     disabled.
    :type enabled: bool
    :ivar last_modified_utc: The last time that this alert has been modified.
    :vartype last_modified_utc: datetime
    :ivar severity: The severity for alerts created by this alert rule.
     Possible values include: 'High', 'Medium', 'Low', 'Informational'
    :vartype severity: str or ~azure.mgmt.securityinsight.models.AlertSeverity
    :ivar tactics: The tactics of the alert rule
    :vartype tactics: list[str or
     ~azure.mgmt.securityinsight.models.AttackTactic]
    """

    _validation = {
        'kind': {'required': True},
        'alert_rule_template_name': {'required': True},
        'description': {'readonly': True},
        'display_name': {'readonly': True},
        'enabled': {'required': True},
        'last_modified_utc': {'readonly': True},
        'severity': {'readonly': True},
        'tactics': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'alert_rule_template_name': {'key': 'properties.alertRuleTemplateName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'last_modified_utc': {'key': 'properties.lastModifiedUtc', 'type': 'iso-8601'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'tactics': {'key': 'properties.tactics', 'type': '[str]'},
    }

    def __init__(self, *, alert_rule_template_name: str, enabled: bool, etag: str=None, **kwargs) -> None:
        super(FusionAlertRule, self).__init__(etag=etag, **kwargs)
        self.alert_rule_template_name = alert_rule_template_name
        self.description = None
        self.display_name = None
        self.enabled = enabled
        self.last_modified_utc = None
        self.severity = None
        self.tactics = None
        self.kind = 'Fusion'
