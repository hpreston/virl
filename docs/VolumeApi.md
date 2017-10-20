# virl.VolumeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_simulation_node_attach_volume_get**](VolumeApi.md#simengine_rest_simulation_node_attach_volume_get) | **GET** /simengine/rest/{simulation}/{node}/attach/{volume} | Attach volume to a running node.
[**simengine_rest_simulation_node_detach_volume_get**](VolumeApi.md#simengine_rest_simulation_node_detach_volume_get) | **GET** /simengine/rest/{simulation}/{node}/detach/{volume} | Detach volume from a running node.


# **simengine_rest_simulation_node_attach_volume_get**
> StdDefsJsondefinitionsnoschema simengine_rest_simulation_node_attach_volume_get(node, simulation, volume)

Attach volume to a running node.

Attach volume to a running node.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.VolumeApi()
node = 'node_example' # str | Node to attach the volume to
simulation = 'simulation_example' # str | Simulation ID
volume = 'volume_example' # str | name of the volume to attach

try: 
    # Attach volume to a running node.
    api_response = api_instance.simengine_rest_simulation_node_attach_volume_get(node, simulation, volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->simengine_rest_simulation_node_attach_volume_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node to attach the volume to | 
 **simulation** | **str**| Simulation ID | 
 **volume** | **str**| name of the volume to attach | 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_simulation_node_detach_volume_get**
> StdDefsJsondefinitionsnoschema simengine_rest_simulation_node_detach_volume_get(node, simulation, volume)

Detach volume from a running node.

Detach volume from a running node.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.VolumeApi()
node = 'node_example' # str | Node to detach the volume from
simulation = 'simulation_example' # str | Simulation ID
volume = 'volume_example' # str | name of the volume to detach

try: 
    # Detach volume from a running node.
    api_response = api_instance.simengine_rest_simulation_node_detach_volume_get(node, simulation, volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->simengine_rest_simulation_node_detach_volume_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node** | **str**| Node to detach the volume from | 
 **simulation** | **str**| Simulation ID | 
 **volume** | **str**| name of the volume to detach | 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

