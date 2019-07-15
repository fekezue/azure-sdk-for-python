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


class IoTSecurityAlertedDevice(Model):
    """Statistic information about the number of alerts per device during the last
    period.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar device_id: Name of the alert type
    :vartype device_id: str
    :ivar alerts_count: the number of alerts raised for this device
    :vartype alerts_count: int
    """

    _validation = {
        'device_id': {'readonly': True},
        'alerts_count': {'readonly': True},
    }

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'alerts_count': {'key': 'alertsCount', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(IoTSecurityAlertedDevice, self).__init__(**kwargs)
        self.device_id = None
        self.alerts_count = None
