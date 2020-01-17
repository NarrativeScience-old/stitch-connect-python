# StreamSchema

A Stream Schema object contains information needed to select a stream and its fields for replication. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema** | **str** | The JSON schema describing the stream’s fields. | [optional] 
**metadata** | [**list[Metadata]**](Metadata.md) | An array of Metadata objects. | [optional] 
**non_discoverable_metadata_keys** | **list[str]** | An array of strings corresponding to &#x60;metadata&#x60; keys that can be modified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


