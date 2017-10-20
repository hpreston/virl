# virl.CatalogApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](CatalogApi.md#root_get) | **GET** / | List all supported URL rules and their associated methods


# **root_get**
> StdDefsJsondefinitionsnoschema root_get()

List all supported URL rules and their associated methods

The catalog request lists all call rules supported by the server. It may be used to verify that a version of STD is installed that supports a particular feature.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.CatalogApi()

try: 
    # List all supported URL rules and their associated methods
    api_response = api_instance.root_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->root_get: %s\n" % e)
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

