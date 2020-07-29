# MixpanelSourceFormProperties

Mixpanel connections read data from the Mixpanel API and correspond to source `type: platform.mixpanel`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_time** | **str** | Defines the time that frequency_in_minutes is \&quot;anchored\&quot; to, which Stitch will use to create the integration&#39;s replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.  | [optional]
**api_secret** | **str** | The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.  |
**attribution_window** | **str** | Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel&#39;s default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.  |
**cron_expression** | **str** | Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source&#39;s default frequency_in_minutes value (60).  | [optional]
**date_window_size** | **str** | Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.  |
**frequency_in_minutes** | **str** | Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440  | [optional]
**project_timezone** | **str** | The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console  |
**select_properties_by_default** | **str** | A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables&#39; records. If set to false, new properties will be ignored.  | [optional]
**start_date** | **str** | The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z  |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


