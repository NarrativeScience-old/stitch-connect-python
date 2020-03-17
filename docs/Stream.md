# Stream

An object representing a table in a data source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_id** | **int** | The stream ID. | [optional]
**selected** | **bool** | Indicates if the stream is selected for replication. Possible values are: null - Only present if a stream has never been selected. Otherwise, this value will be true if selected, and false if de-selected. true - The stream is selected and data will be replicated for all selected fields false - The stream is not selected and data for this stream will not be replicated  | [optional]
**stream_name** | **str** | The name of the stream. This value may not be unique. For example: A database with multiple schemas can have the same stream name in multiple schemas.  | [optional]
**tap_stream_id** | **str** | The unique version of the stream name. For database sources, this value will be the database name, schema name, and table name, combined.  | [optional]
**metadata** | [**StreamLevelMetadata**](StreamLevelMetadata.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


