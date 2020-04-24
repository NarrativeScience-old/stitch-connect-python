# StreamLevelMetadata

Contained in Metadata and Stream objects, the Stream-level Metadata object contains information about a stream’s configuration in Stitch. This includes information about its selection status, Replication Method, Replication Keys, and key properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | For database sources only. The name of the database containing the stream.  | [optional]
**forced_replication_method** | [**ForcedReplicationMethod**](ForcedReplicationMethod.md) |  | [optional]
**is_view** | **bool** | For database sources only. Indicates if the stream is a database view.  | [optional]
**replication_key** | **str** | Indicates the field being used as the stream’s Replication Key.  | [optional]
**replication_method** | **str** | The Replication Method the stream uses to replicate data. Accepted values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication. Note: This method is only available for certain database sources, and requires additional setup to use.  | [optional]
**row_count** | **int** | For database sources only. The number of rows (records) in the stream.  | [optional]
**schema_name** | **str** | For database sources only. The name of the schema containing the stream.  | [optional]
**selected** | **bool** | Indicates whether a stream should be set to replicate. Accepted values are: true - The stream is selected and data for selected fields will be replicated false - The stream is not selected and no data will be replicated  | [optional]
**table_key_properties** | **list[str]** | An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.  | [optional]
**valid_replication_keys** | **list[str]** | An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.  | [optional]
**view_key_properties** | **list[str]** | For database sources only. An array of strings listing the fields that make up the key properties of the view.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


