# virl.TrafficControlApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_shaping_interfaces_simulation_id_delete**](TrafficControlApi.md#simengine_rest_shaping_interfaces_simulation_id_delete) | **DELETE** /simengine/rest/shaping-interfaces/{simulation_id} | Delete interface-level traffic control settings for all links in simulation
[**simengine_rest_shaping_interfaces_simulation_id_get**](TrafficControlApi.md#simengine_rest_shaping_interfaces_simulation_id_get) | **GET** /simengine/rest/shaping-interfaces/{simulation_id} | List interface-level traffic control settings
[**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get**](TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get) | **GET** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id} | List interface-level traffic control settings for a given node in simulation
[**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get**](TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get) | **GET** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id}/{string:iface_id} | List interface-level traffic control setting for a given interface of node in simulation
[**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put**](TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put) | **PUT** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id}/{string:iface_id} | Set interface-level traffic control settings for particular interface
[**simengine_rest_shaping_simulation_id_delete**](TrafficControlApi.md#simengine_rest_shaping_simulation_id_delete) | **DELETE** /simengine/rest/shaping/{simulation_id} | Delete link-level traffic control settings for all links in simulation
[**simengine_rest_shaping_simulation_id_get**](TrafficControlApi.md#simengine_rest_shaping_simulation_id_get) | **GET** /simengine/rest/shaping/{simulation_id} | List link-level traffic control settings
[**simengine_rest_shaping_simulation_id_link_id_delete**](TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_delete) | **DELETE** /simengine/rest/shaping/{simulation_id}/{link_id} | Delete link-level traffic control settings for particular link
[**simengine_rest_shaping_simulation_id_link_id_get**](TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_get) | **GET** /simengine/rest/shaping/{simulation_id}/{link_id} | List link-level traffic control settings for a given link
[**simengine_rest_shaping_simulation_id_link_id_put**](TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_put) | **PUT** /simengine/rest/shaping/{simulation_id}/{link_id} | Set link-level traffic control settings for particular link


# **simengine_rest_shaping_interfaces_simulation_id_delete**
> StdDefsJsondefinitionsinterfacesShaping simengine_rest_shaping_interfaces_simulation_id_delete(simulation_id)

Delete interface-level traffic control settings for all links in simulation

Delete interface-level traffic control settings for all interfaces in simulation

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 

try: 
    # Delete interface-level traffic control settings for all links in simulation
    api_response = api_instance.simengine_rest_shaping_interfaces_simulation_id_delete(simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_interfaces_simulation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionsinterfacesShaping**](StdDefsJsondefinitionsinterfacesShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_interfaces_simulation_id_get**
> StdDefsJsondefinitionsinterfacesShaping simengine_rest_shaping_interfaces_simulation_id_get(simulation_id)

List interface-level traffic control settings

Get interface-level traffic control settings

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 

try: 
    # List interface-level traffic control settings
    api_response = api_instance.simengine_rest_shaping_interfaces_simulation_id_get(simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_interfaces_simulation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionsinterfacesShaping**](StdDefsJsondefinitionsinterfacesShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get**
> StdDefsJsondefinitionsinterfacesShaping simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get(simulation_id, node_id)

List interface-level traffic control settings for a given node in simulation

Get interface-level traffic control settings for a given node in simulation.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
node_id = 'node_id_example' # str | 

try: 
    # List interface-level traffic control settings for a given node in simulation
    api_response = api_instance.simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get(simulation_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionsinterfacesShaping**](StdDefsJsondefinitionsinterfacesShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get**
> StdDefsJsondefinitionsinterfaceShaping simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get(simulation_id, node_id, iface_id)

List interface-level traffic control setting for a given interface of node in simulation

Get interface-level traffic control setting for a given interface of node in simulation.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
node_id = 'node_id_example' # str | 
iface_id = 'iface_id_example' # str | 

try: 
    # List interface-level traffic control setting for a given interface of node in simulation
    api_response = api_instance.simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get(simulation_id, node_id, iface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **node_id** | **str**|  | 
 **iface_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionsinterfaceShaping**](StdDefsJsondefinitionsinterfaceShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put**
> StdDefsJsondefinitionsshaping simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put(simulation_id, node_id, interface_id, shaping)

Set interface-level traffic control settings for particular interface

Set interface-level traffic control settings for a given interface

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
shaping = virl.Shaping() # Shaping | 

try: 
    # Set interface-level traffic control settings for particular interface
    api_response = api_instance.simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put(simulation_id, node_id, interface_id, shaping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **shaping** | [**Shaping**](Shaping.md)|  | 

### Return type

[**StdDefsJsondefinitionsshaping**](StdDefsJsondefinitionsshaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_simulation_id_delete**
> StdDefsJsondefinitionslinksShaping simengine_rest_shaping_simulation_id_delete(simulation_id)

Delete link-level traffic control settings for all links in simulation

Delete link-level traffic control settings for all links in simulation

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 

try: 
    # Delete link-level traffic control settings for all links in simulation
    api_response = api_instance.simengine_rest_shaping_simulation_id_delete(simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_simulation_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionslinksShaping**](StdDefsJsondefinitionslinksShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_simulation_id_get**
> StdDefsJsondefinitionslinksShaping simengine_rest_shaping_simulation_id_get(simulation_id)

List link-level traffic control settings

Get link-level traffic control settings

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 

try: 
    # List link-level traffic control settings
    api_response = api_instance.simengine_rest_shaping_simulation_id_get(simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_simulation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionslinksShaping**](StdDefsJsondefinitionslinksShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_simulation_id_link_id_delete**
> StdDefsJsondefinitionsshaping simengine_rest_shaping_simulation_id_link_id_delete(simulation_id, link_id, shaping)

Delete link-level traffic control settings for particular link

Delete link-level traffic control settings for a given link

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
link_id = 'link_id_example' # str | 
shaping = virl.Shaping() # Shaping | 

try: 
    # Delete link-level traffic control settings for particular link
    api_response = api_instance.simengine_rest_shaping_simulation_id_link_id_delete(simulation_id, link_id, shaping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_simulation_id_link_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **link_id** | **str**|  | 
 **shaping** | [**Shaping**](Shaping.md)|  | 

### Return type

[**StdDefsJsondefinitionsshaping**](StdDefsJsondefinitionsshaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_simulation_id_link_id_get**
> StdDefsJsondefinitionslinksShaping simengine_rest_shaping_simulation_id_link_id_get(simulation_id, link_id)

List link-level traffic control settings for a given link

Get link-level traffic control settings for a given link

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
link_id = 'link_id_example' # str | 

try: 
    # List link-level traffic control settings for a given link
    api_response = api_instance.simengine_rest_shaping_simulation_id_link_id_get(simulation_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_simulation_id_link_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **link_id** | **str**|  | 

### Return type

[**StdDefsJsondefinitionslinksShaping**](StdDefsJsondefinitionslinksShaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_shaping_simulation_id_link_id_put**
> StdDefsJsondefinitionsshaping simengine_rest_shaping_simulation_id_link_id_put(simulation_id, link_id, shaping)

Set link-level traffic control settings for particular link

Set link-level traffic control settings for a given link

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficControlApi()
simulation_id = 'simulation_id_example' # str | 
link_id = 'link_id_example' # str | 
shaping = virl.Shaping() # Shaping | 

try: 
    # Set link-level traffic control settings for particular link
    api_response = api_instance.simengine_rest_shaping_simulation_id_link_id_put(simulation_id, link_id, shaping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficControlApi->simengine_rest_shaping_simulation_id_link_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**|  | 
 **link_id** | **str**|  | 
 **shaping** | [**Shaping**](Shaping.md)|  | 

### Return type

[**StdDefsJsondefinitionsshaping**](StdDefsJsondefinitionsshaping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

