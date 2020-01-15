# Metadata

A Metadata object describes a stream’s schema and the current state of its configuration in Stitch, including its selection status, field inclusion list, Primary Keys, and Replication Method. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breadcrumbs** | **list[str]** | An array of strings describing a path into the schema. For example: A value of [] refers to the entire schema, or stream A value of [\&quot;properties\&quot;, \&quot;&lt;FIELD_NAME&gt;\&quot;] refers to the properties.&lt;FIELD_NAME&gt; portion of the schema. For example: [\&quot;properties\&quot;, \&quot;id\&quot;] would refer to a field named &#x60;id&#x60;  | [optional] 
**metadata** | [**OneOfstreamLevelMetadatafieldLevelMetadata**](OneOfstreamLevelMetadatafieldLevelMetadata.md) | An object containing metadata associated with the breadcrumb. The type of metadata object depends on the breadcrumb: For the entire schema (breadcrumb: []), this will be a Stream-level Metadata object. For an individual field (breadcrumb: [\&quot;properties\&quot;, \&quot;&lt;FIELD_NAME&gt;\&quot;]), this will be a Field-level Metadata object  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


