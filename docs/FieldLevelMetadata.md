# FieldLevelMetadata

Contained in a Metadata object, the Field-level metadata object contains information about a field's inclusion in a stream's field selection list.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inclusion** | **str** | Indicates when a field will be included. Possible values are: automatic - The field is included all the time, regardless of selected-by-default and selected values available - The field is available for selection. The field will be included if selected-by-default or selected is true. unsupported - The field is unsupported and will not be included, regardless of selected-by-default and selected values If a field is unsupported, the &#x60;unsupported-description&#x60; attribute may provide additonal information.  | [optional]
**selected** | **bool** | Indicates whether a field should be included in a stream&#39;s field selection list. This value will be present only if the stream containing the field is selected (selected: true). null - The value has not been set true - The field is selected false - The field is not selected  | [optional]
**selected_by_default** | **bool** | Indicates if a field will be selected by default. Possible values are: null - The value has not been set true - The field is selected by default and is included regardless of the &#x60;selected&#x60; value false - The field is not selected by default. The field will be included if the &#x60;selected value&#x60; is true.  | [optional]
**sql_datatype** | **str** | For database sources only. The data type of a column from a database.  | [optional]
**field_exclusions** | **object** | A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected. For example: If the metadata for a DeviceOS field contains a fieldExclusion of [\&quot;properties\&quot;:\&quot;ImpressionLostToBidPercent\&quot;], then the DeviceOS and ImpressionLostToBidPercent fields cannot be selected together in the stream.  | [optional]
**unsupported_description** | **str** | The reason a field is unsupported (&#x60;inclusion&#x60;: unsupported). Note: This is not available for all sources.  | [optional]
**tap_google_analytics_cubes** | **list[str]** | For Google Analytics sources only. An array of strings containing the ‘cubes&#39; the field is a part of. A cube is a group of metrics and dimensions that are compatible together.  | [optional]
**tap_google_analytics_group** | **str** | For Google Analytics sources only. The group the field belongs to. Possible values are: - Ad Exchange - Adsense - Adwords - App Tracking - Audience - Channel Grouping - Content Experiments - Content Grouping - Custom Variables or Columns - DoubleClick Bid Manager - DoubleClick Campaign Manager - DoubleClick Search - DoubleClick for Publishers - DoubleClick for Publishers Backfill - Ecommerce - Event Tracking - Exceptions - Geo Network - Goal Conversions - Internal Search - Lifetime Value and Cohorts - Page Tracking - Platform or Device - Publisher - Report Fields - Session - Site Speed - Social Activities - Social Interactions - System - Time - Traffic Sources - User - User Timings  | [optional]
**behavior** | **str** | For Google Analytics and Google Ads sources only. The type of field. Possible values are: - ATTRIBUTE - Goolgle Ads sources only - METRIC - DIMENSION - Google Analytics sources only - SEGMENT - Goolgle Ads sources only Note: This property won&#39;t be present for Google Analytics fields where tap_google_analytics.group: Report Fields.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


