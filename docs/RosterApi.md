# virl.RosterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roster_rest_get**](RosterApi.md#roster_rest_get) | **GET** /roster/rest/ | Get GUI-related information on all user’s simulations
[**roster_rest_test_get**](RosterApi.md#roster_rest_test_get) | **GET** /roster/rest/test | Verify the user is authenticated and return roster API version


# **roster_rest_get**
> StdDefsJsondefinitionsnoschema roster_rest_get(uuid=uuid)

Get GUI-related information on all user’s simulations

Get GUI-related information on all user’s simulations. Also returns an UUID marker for the roster (user endpoint) state; if an UUID parameter is provided by the client, the service shall wait until the internal value changes, or an internal timeout occurs to avoid blocking the server. The format is a JSON Object with keys being dot-separated hierarchical elements of a tree view of the simulations. The values are JSON Objects with arbitrary attributes, some of which are recognized by the GUI.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.RosterApi()
uuid = 'uuid_example' # str | UUID of the roster state (optional)

try: 
    # Get GUI-related information on all user’s simulations
    api_response = api_instance.roster_rest_get(uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RosterApi->roster_rest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the roster state | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roster_rest_test_get**
> StdDefsJsondefinitionsnoschema roster_rest_test_get()

Verify the user is authenticated and return roster API version

The Roster area is meant as a single unified service to power the VMMaestro GUI’s simulation runtime functionality. The roster collects GUI-required information on all launched simulations of the requesting user.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.RosterApi()

try: 
    # Verify the user is authenticated and return roster API version
    api_response = api_instance.roster_rest_test_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RosterApi->roster_rest_test_get: %s\n" % e)
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

