# virl.SnapshotApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_snapshot_simulation_node_post**](SnapshotApi.md#simengine_rest_snapshot_simulation_node_post) | **POST** /simengine/rest/snapshot/{simulation}/{node} | Create snapshot of a node


# **simengine_rest_snapshot_simulation_node_post**
> StdDefsJsondefinitionsnoschema simengine_rest_snapshot_simulation_node_post(simulation, node, name=name)

Create snapshot of a node

Create snapshot of a node. The snapshot will be a private image (visible only inside the same project) named as project-subtype-imagename.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SnapshotApi()
simulation = 'simulation_example' # str | Simulation ID
node = 'node_example' # str | Node name
name = 'null' # str | last part of the created image name (optional) (default to null)

try: 
    # Create snapshot of a node
    api_response = api_instance.simengine_rest_snapshot_simulation_node_post(simulation, node, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->simengine_rest_snapshot_simulation_node_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **node** | **str**| Node name | 
 **name** | **str**| last part of the created image name | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

