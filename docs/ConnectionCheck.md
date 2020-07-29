# ConnectionCheck

A Connection Check object shows the results from a test of a connection's parameters. This is a test performed by Stitch that checks the configuration of a source's connection parameters. The nature of the test varies by connection type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connection check job. | [optional]
**mode** | **str** | This value will always be &#x60;check&#x60;. | [optional]
**status** | **str** | The status of the connection check job. Possible values are: - running - succeeded - failed  | [optional]
**start_time** | **str** | The date and time the connection check job started. | [optional]
**completion_time** | **str** | The date and time the connection check job was completed. | [optional]
**error** | **bool** | Indicates if the connection check job resulted in an error. This will be true if any of the exit_status properties are non-zero.  | [optional]
**check_exit_status** | **int** | The exit status of the connection check job. Possible values are: null - The connection check job is still running 0 - The connection check job was successful 1 - The connection check job was unsuccessful  | [optional]
**discovery_exit_status** | **int** | The exit status of the discovery portion of the connection check job. Possible values are: null - Job is still running 0 - Job was successful Any non-zero value - Discovery failed  | [optional]
**discovery_error_message** | **str** | Exception message raised when discovery failed during the connection check job. If successful, this will be null.  | [optional]
**tap_exit_status** | **int** | The exit status of the tap. Possible values are: null - Tap is still running 0 - Tap was successful Any non-zero value - Tap failed  | [optional]
**tap_error_message** | **str** | Exception message raised when extraction failed during the job. If successful, this will be null.  | [optional]
**target_exit_status** | **int** | The exit status of the target portion of the connection check job. Possible values are: null - Target is still running 0 - Target was successful Any non-zero value - Target failed  | [optional]
**target_error_message** | **str** | This value will always be null. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


