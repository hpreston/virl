# virl.LinksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_link_simulation_id_get**](LinksApi.md#simengine_rest_link_simulation_id_get) | **GET** /simengine/rest/link/{simulation_id} | Get link identifiers for selected simulation
[**simengine_rest_link_simulation_id_stringnode_id_iface_id_get**](LinksApi.md#simengine_rest_link_simulation_id_stringnode_id_iface_id_get) | **GET** /simengine/rest/link/{simulation_id}/{string:node_id}/{iface_id} | Get info about a given link


# **simengine_rest_link_simulation_id_get**
> StdDefsJsondefinitionslinks simengine_rest_link_simulation_id_get(simulation_id)

Get link identifiers for selected simulation

Get link identifiers for selected simulation

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.LinksApi()
simulation_id = 'simulation_id_example' # str | 

try: 
    # Get link identifiers for selected simulation
    api_response = api_instance.simengine_rest_link_simulation_id_get(simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->simengine_rest_link_simulation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionslinks**](StdDefsJsondefinitionslinks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_link_simulation_id_stringnode_id_iface_id_get**
> StdDefsJsondefinitionslinks simengine_rest_link_simulation_id_stringnode_id_iface_id_get(simulation_id, node_id, link_id)

Get info about a given link

Get info about a given link

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.LinksApi()
simulation_id = 'simulation_id_example' # str | 
node_id = 'node_id_example' # str | 
link_id = 'link_id_example' # str | 

try: 
    # Get info about a given link
    api_response = api_instance.simengine_rest_link_simulation_id_stringnode_id_iface_id_get(simulation_id, node_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->simengine_rest_link_simulation_id_stringnode_id_iface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **node_id** | **str**|  | 
 **link_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionslinks**](StdDefsJsondefinitionslinks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

