# FieldLevelMetadata

Contained in a Metadata object, the Field-level metadata object contains information about a field’s inclusion in a stream’s field selection list. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inclusion** | **str** | Indicates when a field will be included. Possible values are: automatic - The field is included all the time, regardless of selected-by-default and selected values available - The field is available for selection. The field will be included if selected-by-default or selected is true. unsupported - The field is unsupported and will not be included, regardless of selected-by-default and selected values If a field is unsupported, the &#x60;unsupported-description&#x60; attribute may provide additonal information.  | [optional] 
**selected** | **bool** | Indicates whether a field should be included in a stream’s field selection list. This value will be present only if the stream containing the field is selected (selected: true). null - The value has not been set true - The field is selected false - The field is not selected  | [optional] 
**selected_by_default** | **bool** | Indicates if a field will be selected by default. Possible values are: null - The value has not been set true - The field is selected by default and is included regardless of the &#x60;selected&#x60; value false - The field is not selected by default. The field will be included if the &#x60;selected value&#x60; is true.  | [optional] 
**sql_datatype** | **str** | For database sources only. The data type of a column from a database.  | [optional] 
**field_exclusions** | **object** | A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected. For example: If the metadata for a DeviceOS field contains a fieldExclusion of [\&quot;properties\&quot;:\&quot;ImpressionLostToBidPercent\&quot;], then the DeviceOS and ImpressionLostToBidPercent fields cannot be selected together in the stream.  | [optional] 
**unsupported_description** | **str** | The reason a field is unsupported (&#x60;inclusion&#x60;: unsupported). Note: This is not available for all sources.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

