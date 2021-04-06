'''
https://cloud.google.com/compute/docs/reference/rest/v1/firewalls/list
gcloud compute firewall-rules list
export GOOGLE_APPLICATION_CREDENTIALS="/Users/junsong/Documents/g-hash-community-ec3fd721313f.json"

export GOOGLE_APPLICATION_CREDENTIALS="/Users/junsong/Documents/inner-tools-256713-7dbab302aa66.json"

'''
from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'g-hash-community'  # TODO: Update placeholder value.
#project = 'inner-tools-256713'
request = service.firewalls().list(project=project)
while request is not None:
    response = request.execute()

    for firewall in response['items']:
        # TODO: Change code below to process each `firewall` resource:
        pprint(firewall)

    request = service.firewalls().list_next(previous_request=request, previous_response=response)


