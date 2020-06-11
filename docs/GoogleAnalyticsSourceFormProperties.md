# GoogleAnalyticsSourceFormProperties

Google Analytics connections read data from the Google Analytics API and correspond to source type: platform.google-analytics.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_time** | **str** | Defines the time that frequency_in_minutes is “anchored” to, which Stitch will use to create the integration’s replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.  | [optional]
**client_id** | **str** | The secure OAuth 2.0 identifier for the client application.  | [optional]
**client_secret** | **str** | The secure OAuth 2.0 secret key for the client application.  | [optional]
**cron_expression** | **str** | Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source’s default frequency_in_minutes value (60).  | [optional]
**frequency_in_minutes** | **str** | Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440  | [optional]
**quota_user** | **str** | Note: This is a read-only property and will be returned when the Google Analytics object is successfully created. Including it in POST or PUT requests will result in InvalidProperties errors.  | [optional]
**refresh_token** | **str** | The OAuth 2.0 refresh token used to access the Google API. | [optional]
**report_definitions** | [**list[GoogleAnalyticsSourceFormPropertiesReportDefinitions]**](GoogleAnalyticsSourceFormPropertiesReportDefinitions.md) | An array of objects, each object pertaining to a custom report you want to create. Note: Metrics and dimensions for each report can be selected when the source proceeds to the field_selection step.  | [optional]
**start_date** | **str** | The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


