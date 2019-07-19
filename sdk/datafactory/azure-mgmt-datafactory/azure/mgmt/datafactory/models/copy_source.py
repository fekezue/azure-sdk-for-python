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


class CopySource(Model):
    """A copy activity source.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AmazonRedshiftSource, GoogleAdWordsSource,
    OracleServiceCloudSource, DynamicsAXSource, ResponsysSource,
    SalesforceMarketingCloudSource, VerticaSource, NetezzaSource, ZohoSource,
    XeroSource, SquareSource, SparkSource, ShopifySource, ServiceNowSource,
    QuickBooksSource, PrestoSource, PhoenixSource, PaypalSource, MarketoSource,
    MariaDBSource, MagentoSource, JiraSource, ImpalaSource, HubspotSource,
    HiveSource, HBaseSource, GreenplumSource, GoogleBigQuerySource,
    EloquaSource, DrillSource, CouchbaseSource, ConcurSource,
    AzurePostgreSqlSource, AmazonMWSSource, HttpSource, AzureBlobFSSource,
    AzureDataLakeStoreSource, Office365Source, CosmosDbMongoDbApiSource,
    MongoDbV2Source, MongoDbSource, CassandraSource, WebSource, TeradataSource,
    OracleSource, AzureDataExplorerSource, AzureMySqlSource, HdfsSource,
    FileSystemSource, SqlDWSource, SqlMISource, AzureSqlSource,
    SqlServerSource, SqlSource, RestSource, SapTableSource, SapOpenHubSource,
    SapHanaSource, SapEccSource, SapCloudForCustomerSource,
    SalesforceServiceCloudSource, SalesforceSource, MicrosoftAccessSource,
    InformixSource, RelationalSource, CommonDataServiceForAppsSource,
    DynamicsCrmSource, DynamicsSource, DocumentDbCollectionSource, BlobSource,
    AzureTableSource, BinarySource, DelimitedTextSource, ParquetSource,
    AvroSource

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'AmazonRedshiftSource': 'AmazonRedshiftSource', 'GoogleAdWordsSource': 'GoogleAdWordsSource', 'OracleServiceCloudSource': 'OracleServiceCloudSource', 'DynamicsAXSource': 'DynamicsAXSource', 'ResponsysSource': 'ResponsysSource', 'SalesforceMarketingCloudSource': 'SalesforceMarketingCloudSource', 'VerticaSource': 'VerticaSource', 'NetezzaSource': 'NetezzaSource', 'ZohoSource': 'ZohoSource', 'XeroSource': 'XeroSource', 'SquareSource': 'SquareSource', 'SparkSource': 'SparkSource', 'ShopifySource': 'ShopifySource', 'ServiceNowSource': 'ServiceNowSource', 'QuickBooksSource': 'QuickBooksSource', 'PrestoSource': 'PrestoSource', 'PhoenixSource': 'PhoenixSource', 'PaypalSource': 'PaypalSource', 'MarketoSource': 'MarketoSource', 'MariaDBSource': 'MariaDBSource', 'MagentoSource': 'MagentoSource', 'JiraSource': 'JiraSource', 'ImpalaSource': 'ImpalaSource', 'HubspotSource': 'HubspotSource', 'HiveSource': 'HiveSource', 'HBaseSource': 'HBaseSource', 'GreenplumSource': 'GreenplumSource', 'GoogleBigQuerySource': 'GoogleBigQuerySource', 'EloquaSource': 'EloquaSource', 'DrillSource': 'DrillSource', 'CouchbaseSource': 'CouchbaseSource', 'ConcurSource': 'ConcurSource', 'AzurePostgreSqlSource': 'AzurePostgreSqlSource', 'AmazonMWSSource': 'AmazonMWSSource', 'HttpSource': 'HttpSource', 'AzureBlobFSSource': 'AzureBlobFSSource', 'AzureDataLakeStoreSource': 'AzureDataLakeStoreSource', 'Office365Source': 'Office365Source', 'CosmosDbMongoDbApiSource': 'CosmosDbMongoDbApiSource', 'MongoDbV2Source': 'MongoDbV2Source', 'MongoDbSource': 'MongoDbSource', 'CassandraSource': 'CassandraSource', 'WebSource': 'WebSource', 'TeradataSource': 'TeradataSource', 'OracleSource': 'OracleSource', 'AzureDataExplorerSource': 'AzureDataExplorerSource', 'AzureMySqlSource': 'AzureMySqlSource', 'HdfsSource': 'HdfsSource', 'FileSystemSource': 'FileSystemSource', 'SqlDWSource': 'SqlDWSource', 'SqlMISource': 'SqlMISource', 'AzureSqlSource': 'AzureSqlSource', 'SqlServerSource': 'SqlServerSource', 'SqlSource': 'SqlSource', 'RestSource': 'RestSource', 'SapTableSource': 'SapTableSource', 'SapOpenHubSource': 'SapOpenHubSource', 'SapHanaSource': 'SapHanaSource', 'SapEccSource': 'SapEccSource', 'SapCloudForCustomerSource': 'SapCloudForCustomerSource', 'SalesforceServiceCloudSource': 'SalesforceServiceCloudSource', 'SalesforceSource': 'SalesforceSource', 'MicrosoftAccessSource': 'MicrosoftAccessSource', 'InformixSource': 'InformixSource', 'RelationalSource': 'RelationalSource', 'CommonDataServiceForAppsSource': 'CommonDataServiceForAppsSource', 'DynamicsCrmSource': 'DynamicsCrmSource', 'DynamicsSource': 'DynamicsSource', 'DocumentDbCollectionSource': 'DocumentDbCollectionSource', 'BlobSource': 'BlobSource', 'AzureTableSource': 'AzureTableSource', 'BinarySource': 'BinarySource', 'DelimitedTextSource': 'DelimitedTextSource', 'ParquetSource': 'ParquetSource', 'AvroSource': 'AvroSource'}
    }

    def __init__(self, **kwargs):
        super(CopySource, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.source_retry_count = kwargs.get('source_retry_count', None)
        self.source_retry_wait = kwargs.get('source_retry_wait', None)
        self.max_concurrent_connections = kwargs.get('max_concurrent_connections', None)
        self.type = None
