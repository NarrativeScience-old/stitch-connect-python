# MetadataObject

An object containing metadata associated with the breadcrumb. The type of metadata object depends on the breadcrumb: For the entire schema (breadcrumb: []), this will be a Stream-level Metadata object. For an individual field (breadcrumb: [\"properties\", \"<FIELD_NAME>\"]), this will be a Field-level Metadata object
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
**selected** | **bool** | Indicates whether a field should be included in a stream’s field selection list. This value will be present only if the stream containing the field is selected (selected: true). null - The value has not been set true - The field is selected false - The field is not selected  | [optional]
**table_key_properties** | **list[str]** | An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.  | [optional]
**valid_replication_keys** | **list[str]** | An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.  | [optional]
**view_key_properties** | **list[str]** | For database sources only. An array of strings listing the fields that make up the key properties of the view.  | [optional]
**inclusion** | **str** | Indicates when a field will be included. Possible values are: automatic - The field is included all the time, regardless of selected-by-default and selected values available - The field is available for selection. The field will be included if selected-by-default or selected is true. unsupported - The field is unsupported and will not be included, regardless of selected-by-default and selected values If a field is unsupported, the &#x60;unsupported-description&#x60; attribute may provide additonal information.  | [optional]
**selected_by_default** | **bool** | Indicates if a field will be selected by default. Possible values are: null - The value has not been set true - The field is selected by default and is included regardless of the &#x60;selected&#x60; value false - The field is not selected by default. The field will be included if the &#x60;selected value&#x60; is true.  | [optional]
**sql_datatype** | **str** | For database sources only. The data type of a column from a database.  | [optional]
**field_exclusions** | **object** | A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected. For example: If the metadata for a DeviceOS field contains a fieldExclusion of [\&quot;properties\&quot;:\&quot;ImpressionLostToBidPercent\&quot;], then the DeviceOS and ImpressionLostToBidPercent fields cannot be selected together in the stream.  | [optional]
**unsupported_description** | **str** | The reason a field is unsupported (&#x60;inclusion&#x60;: unsupported). Note: This is not available for all sources.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


