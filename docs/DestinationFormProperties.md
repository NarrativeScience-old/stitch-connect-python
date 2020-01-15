# DestinationFormProperties

Parameters for connecting to the destination, excluding any sensitive credentials. The parameters must adhere to the type of destination. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_delimiter** | **str** | csv delimiter character | [optional] 
**output_file_format** | **str** | Defines the type of file Stitch will write to the bucket. Possible values are: - csv, which will use CSV (.csv) files - jsonl, which will use JSON (.jsonl) files  | [optional] 
**s3_bucket** | **str** | The name of the Amazon S3 bucket Stitch will write to. | [optional] 
**azure_storage_account_token** | **str** | An Azure Storage Access Key. This is used to access Azure Blob Storage, which Stitch uses to stage data for Polybase before loading it into an Azure SQL Data Warehouse destination.  | [optional] 
**azure_storage_sas_url** | **str** | An Azure Blob service Shared Access Signature (SAS) URL, which is used to grant Stitch restricted access to Azure Storage resources. These resources are used to load data into an Azure SQL Data Warehouse destination.  | [optional] 
**database** | **str** | The name of the logical database to connect to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


