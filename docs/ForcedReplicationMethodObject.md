# ForcedReplicationMethodObject

A stream will sometimes be forced to use a particular Replication Method. This describes the replication method and the reason for the requirement. This is only used for Salesforce sources. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the forced Replication Method | [optional] 
**replication_method** | **str** | Indicates which Replication Method is required for the stream. Possible values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


