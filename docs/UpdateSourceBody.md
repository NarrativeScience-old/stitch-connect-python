# UpdateSourceBody

Parameters for updating a data source
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into.  | [optional] 
**paused_at** | **str** | The time the source was paused. This field must contain an ISO 8601-compliant date. Note: Providing any value - past, present, or future - for this property will pause the source immediately if the request is successful.  | [optional] 
**properties** | [**SourceFormProperties**](SourceFormProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


