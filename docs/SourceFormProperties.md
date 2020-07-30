# SourceFormProperties

Parameters for connecting to the source, excluding any sensitive credentials. The parameters must adhere to the type of source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_time** | **str** | Defines the time that frequency_in_minutes is \&quot;anchored\&quot; to, which Stitch will use to create the integration&#39;s replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.  | [optional]
**api_type** | **str** | The Salesforce API Stitch should use to extract data. Possible values are REST or BULK.  | [optional]
**client_id** | **str** | The secure OAuth 2.0 identifier for the client application.  | [optional]
**client_secret** | **str** | The secure OAuth 2.0 secret key for the client application.  | [optional]
**cron_expression** | **str** | Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source&#39;s default frequency_in_minutes value (60).  | [optional]
**frequency_in_minutes** | **str** | Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440  | [optional]
**instance_url** | **str** | The url of the instance to connect to. | [optional]
**is_sandbox** | **str** | If &#x60;true&#x60;, the Salesforce account being connected is a sandbox. | [optional]
**quota_percent_per_run** | **str** | The maximum percentage of Salesforce API quota allowed per replication job.  | [optional]
**quota_percent_total** | **str** | The maximum percentage of Salesforce API quota allowed per day.  | [optional]
**refresh_token** | **str** | The OAuth 2.0 refresh token used to access the Google API. | [optional]
**select_fields_by_default** | **str** | If &#x60;true&#x60;, Stitch will automatically set new fields added in Salesforce to replicate.  | [optional]
**start_date** | **str** | The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z  | [optional]
**quota_user** | **str** | Note: This is a read-only property and will be returned when the Google Analytics object is successfully created. Including it in POST or PUT requests will result in InvalidProperties errors.  | [optional]
**report_definitions** | [**list[GoogleAnalyticsSourceFormPropertiesReportDefinitions]**](GoogleAnalyticsSourceFormPropertiesReportDefinitions.md) | An array of objects, each object pertaining to a custom report you want to create. Note: Metrics and dimensions for each report can be selected when the source proceeds to the field_selection step.  | [optional]
**api_secret** | **str** | The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.  | [optional]
**attribution_window** | **str** | Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel&#39;s default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.  | [optional]
**date_window_size** | **str** | Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.  | [optional]
**project_timezone** | **str** | The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console  | [optional]
**select_properties_by_default** | **str** | A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables&#39; records. If set to false, new properties will be ignored.  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


