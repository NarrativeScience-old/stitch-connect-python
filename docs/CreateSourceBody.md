# CreateSourceBody

Request body for creating a new source
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into.  | 
**type** | **str** | The source type. For example: platform.marketo or platform.hubspot.  | 
**name** | **str** | The destination schema name that the data from this source will be loaded into. Names must: - Contain only lowercase alphanumerics and underscores - Be unique within each Stitch client account  | [optional] 
**properties** | [**SourceFormProperties**](SourceFormProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


