# SalesforceSourceFormProperties

Salesforce connections read data from the Salesforce API and correspond to source type: platform.salesforce.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_time** | **str** | Defines the time that frequency_in_minutes is \&quot;anchored\&quot; to, which Stitch will use to create the integration&#39;s replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.  | [optional]
**api_type** | **str** | The Salesforce API Stitch should use to extract data. Possible values are REST or BULK.  | [optional]
**client_id** | **str** | The secure OAuth 2.0 identifier for the client application.  | [optional]
**client_secret** | **str** | The secure OAuth 2.0 secret key for the client application.  | [optional]
**cron_expression** | **str** | Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source&#39;s default frequency_in_minutes value (60).  | [optional]
**frequency_in_minutes** | **str** | Defines how often, in minutes, Stitch should attempt to replicate data from Salesforce. Accepted values are: - 30 - 60 - 360 - 720 - 1440  | [optional]
**instance_url** | **str** | The url of the instance to connect to. | [optional]
**is_sandbox** | **str** | If &#x60;true&#x60;, the Salesforce account being connected is a sandbox. | [optional]
**quota_percent_per_run** | **str** | The maximum percentage of Salesforce API quota allowed per replication job.  | [optional]
**quota_percent_total** | **str** | The maximum percentage of Salesforce API quota allowed per day.  | [optional]
**refresh_token** | **str** | The OAuth 2.0 refresh token used to access the Salesforce API. | [optional]
**select_fields_by_default** | **str** | If &#x60;true&#x60;, Stitch will automatically set new fields added in Salesforce to replicate.  | [optional]
**start_date** | **str** | The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


