# virl.InterfacesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_interfaces_simulation_get**](InterfacesApi.md#simengine_rest_interfaces_simulation_get) | **GET** /simengine/rest/interfaces/{simulation} | List simulation interfaces.
[**simengine_rest_update_interfaces_simulation_put**](InterfacesApi.md#simengine_rest_update_interfaces_simulation_put) | **PUT** /simengine/rest/update/interfaces/{simulation} | Update simulation nodes interfaces admin_state.


# **simengine_rest_interfaces_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_interfaces_simulation_get(simulation, nodes=nodes, networks=networks, interfaces=interfaces)

List simulation interfaces.

List simulation interfaces.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.InterfacesApi()
simulation = 'simulation_example' # str | Simulation ID
nodes = ['null'] # list[str] | select nodes for return by name or XPath, defaults to all nodes (optional) (default to null)
networks = ['null'] # list[str] | select networks for return by name or XPath, defaults to all networks (optional) (default to null)
interfaces = ['null'] # list[str] | select interfaces for return by name or XPath, defaults to all interfaces (optional) (default to null)

try: 
    # List simulation interfaces.
    api_response = api_instance.simengine_rest_interfaces_simulation_get(simulation, nodes=nodes, networks=networks, interfaces=interfaces)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->simengine_rest_interfaces_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **nodes** | [**list[str]**](str.md)| select nodes for return by name or XPath, defaults to all nodes | [optional] [default to null]
 **networks** | [**list[str]**](str.md)| select networks for return by name or XPath, defaults to all networks | [optional] [default to null]
 **interfaces** | [**list[str]**](str.md)| select interfaces for return by name or XPath, defaults to all interfaces | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_update_interfaces_simulation_put**
> StdDefsJsondefinitionsnoschema simengine_rest_update_interfaces_simulation_put(simulation, link_state, nodes=nodes, networks=networks, interfaces=interfaces)

Update simulation nodes interfaces admin_state.

Update simulation nodes interfaces admin_state.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.InterfacesApi()
simulation = 'simulation_example' # str | Simulation ID
link_state = 56 # int | Interface admin_state (0 = down, 1 = up)
nodes = ['null'] # list[str] | select nodes for return by name or XPath, defaults to all nodes (optional) (default to null)
networks = ['null'] # list[str] | select networks for return by name or XPath, defaults to all networks (optional) (default to null)
interfaces = ['null'] # list[str] | select interfaces for return by name or XPath, defaults to all interfaces (optional) (default to null)

try: 
    # Update simulation nodes interfaces admin_state.
    api_response = api_instance.simengine_rest_update_interfaces_simulation_put(simulation, link_state, nodes=nodes, networks=networks, interfaces=interfaces)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->simengine_rest_update_interfaces_simulation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **link_state** | **int**| Interface admin_state (0 &#x3D; down, 1 &#x3D; up) | 
 **nodes** | [**list[str]**](str.md)| select nodes for return by name or XPath, defaults to all nodes | [optional] [default to null]
 **networks** | [**list[str]**](str.md)| select networks for return by name or XPath, defaults to all networks | [optional] [default to null]
 **interfaces** | [**list[str]**](str.md)| select interfaces for return by name or XPath, defaults to all interfaces | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

