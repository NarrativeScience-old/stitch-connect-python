# Metadata

A Metadata object describes a stream's schema and the current state of its configuration in Stitch, including its selection status, field inclusion list, Primary Keys, and Replication Method.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breadcrumb** | **list[str]** | An array of strings describing a path into the schema. For example: A value of [] refers to the entire schema, or stream A value of [\&quot;properties\&quot;, \&quot;&lt;FIELD_NAME&gt;\&quot;] refers to the properties.&lt;FIELD_NAME&gt; portion of the schema. For example: [\&quot;properties\&quot;, \&quot;id\&quot;] would refer to a field named &#x60;id&#x60;  |
**metadata** | [**MetadataObject**](MetadataObject.md) |  |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


