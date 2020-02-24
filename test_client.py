from __future__ import print_function
import time
import asyncio
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint
configuration = stitch_connect_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'at_b555274fc8674b320d55090a07cb5955'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))
create_source_body = stitch_connect_client.CreateSourceBody(
    display_name="foofoo",
    type="platform.salesforce",
    properties=stitch_connect_client.SalesforceSourceFormProperties(
        api_type="BULK",
        client_id="test_client_id",
        client_secret="test_client_secret",
        # The cron_expression property will override the default frequency_in_minutes
        cron_expression="0 0/15 0 ? * * *",
        frequency_in_minutes="30",
        instance_url="url",
        is_sandbox="true",
        select_fields_by_default="true",
        start_date="2017-01-01T00:00:00Z",
        refresh_token="token"
    )
) # CreateSourceBody | Request body to create a new source

async def call():
    try:
        # Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed.
        api_response = await api_instance.create_source(create_source_body)
        pprint(api_response)
    except ApiException as e:
        import ipdb; ipdb.set_trace()
        print("Exception when calling api: %s\n" % e)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(call())
