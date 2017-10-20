# virl.AutonetkitApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ank_rest_process_post**](AutonetkitApi.md#ank_rest_process_post) | **POST** /ank/rest/process | Process a VIRL XML Topology
[**ank_rest_test_get**](AutonetkitApi.md#ank_rest_test_get) | **GET** /ank/rest/test | Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version


# **ank_rest_process_post**
> object ank_rest_process_post(debug=debug, uuid=uuid, session=session)

Process a VIRL XML Topology

This call processes a VIRL XML Topology file with AutoNetkit and assign initial configuration into each node’s config extension entry, based on parameters included in other extension entries throughout the file. In case the AutoNetkit subprocess returns with an error, the response will contain the log of the AutoNetkit process. Since AutoNetkit’s logs may be vital even in case of a successful configuration, the logs may be requested to be returned in a MIME multipart response. This behaviour can be turned on via the Accept HTTP header

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AutonetkitApi()
debug = 'None' # str | Enable debug logging (optional) (default to None)
uuid = 'None' # str | Identifier for AutoNetkit Visualization Web UI (optional) (default to None)
session = 'None' # str | DEPRECATED, the same as uuid (optional) (default to None)

try: 
    # Process a VIRL XML Topology
    api_response = api_instance.ank_rest_process_post(debug=debug, uuid=uuid, session=session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutonetkitApi->ank_rest_process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debug** | **str**| Enable debug logging | [optional] [default to None]
 **uuid** | **str**| Identifier for AutoNetkit Visualization Web UI | [optional] [default to None]
 **session** | **str**| DEPRECATED, the same as uuid | [optional] [default to None]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/xml, multipart/mixed
 - **Accept**: text/xml, multipart/mixed

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ank_rest_test_get**
> StdDefsJsondefinitionsnoschema ank_rest_test_get()

Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version

Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AutonetkitApi()

try: 
    # Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
    api_response = api_instance.ank_rest_test_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutonetkitApi->ank_rest_test_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

