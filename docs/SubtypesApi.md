# virl.SubtypesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_subtypes_get**](SubtypesApi.md#simengine_rest_subtypes_get) | **GET** /simengine/rest/subtypes | List supported VM subtypes


# **simengine_rest_subtypes_get**
> StdDefsJsondefinitionsnoschema simengine_rest_subtypes_get()

List supported VM subtypes

Get information on all supported VM node subtypes. This call is mainly intended for the GUI at topology design time.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SubtypesApi()

try: 
    # List supported VM subtypes
    api_response = api_instance.simengine_rest_subtypes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtypesApi->simengine_rest_subtypes_get: %s\n" % e)
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

