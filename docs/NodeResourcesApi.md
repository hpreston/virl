# virl.NodeResourcesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openstack_rest_create_port_post**](NodeResourcesApi.md#openstack_rest_create_port_post) | **POST** /openstack/rest/create-port | Create a port on an OpenStack network
[**openstack_rest_flavors_get**](NodeResourcesApi.md#openstack_rest_flavors_get) | **GET** /openstack/rest/flavors | Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
[**openstack_rest_images_get**](NodeResourcesApi.md#openstack_rest_images_get) | **GET** /openstack/rest/images | Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
[**openstack_rest_networks_get**](NodeResourcesApi.md#openstack_rest_networks_get) | **GET** /openstack/rest/networks | Return information about OpenStack networks.
[**openstack_rest_ports_network_name_get**](NodeResourcesApi.md#openstack_rest_ports_network_name_get) | **GET** /openstack/rest/ports/{network_name} | Return information about the ports of an OpenStack network.
[**openstack_rest_test_get**](NodeResourcesApi.md#openstack_rest_test_get) | **GET** /openstack/rest/test | Verify the user is authenticated and return openstack API version.
[**openstack_rest_volumes_get**](NodeResourcesApi.md#openstack_rest_volumes_get) | **GET** /openstack/rest/volumes | Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.


# **openstack_rest_create_port_post**
> StdDefsJsondefinitionsnoschema openstack_rest_create_port_post(network_name, port_name, tenant_name=tenant_name, fixed_ip=fixed_ip, floating_ip=floating_ip)

Create a port on an OpenStack network

Create a port on an OpenStack network

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()
network_name = 'network_name_example' # str | name of the network on which the port should be created
port_name = 'port_name_example' # str | name of the new port
tenant_name = 'null' # str | port owner; if not specified, the current user's project will be used (optional) (default to null)
fixed_ip = 'null' # str | custom fixed IP of the new port (optional) (default to null)
floating_ip = 'null' # str | custom floating IP of the new port (optional) (default to null)

try: 
    # Create a port on an OpenStack network
    api_response = api_instance.openstack_rest_create_port_post(network_name, port_name, tenant_name=tenant_name, fixed_ip=fixed_ip, floating_ip=floating_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_create_port_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| name of the network on which the port should be created | 
 **port_name** | **str**| name of the new port | 
 **tenant_name** | **str**| port owner; if not specified, the current user&#39;s project will be used | [optional] [default to null]
 **fixed_ip** | **str**| custom fixed IP of the new port | [optional] [default to null]
 **floating_ip** | **str**| custom floating IP of the new port | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openstack_rest_flavors_get**
> StdDefsJsondefinitionsnoschema openstack_rest_flavors_get()

Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.

Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()

try: 
    # Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
    api_response = api_instance.openstack_rest_flavors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_flavors_get: %s\n" % e)
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

# **openstack_rest_images_get**
> StdDefsJsondefinitionsnoschema openstack_rest_images_get()

Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.

Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()

try: 
    # Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
    api_response = api_instance.openstack_rest_images_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_images_get: %s\n" % e)
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

# **openstack_rest_networks_get**
> StdDefsJsondefinitionsnoschema openstack_rest_networks_get()

Return information about OpenStack networks.

Return information about OpenStack networks.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()

try: 
    # Return information about OpenStack networks.
    api_response = api_instance.openstack_rest_networks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_networks_get: %s\n" % e)
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

# **openstack_rest_ports_network_name_get**
> StdDefsJsondefinitionsnoschema openstack_rest_ports_network_name_get(network_name)

Return information about the ports of an OpenStack network.

Return information about the ports of an OpenStack network.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()
network_name = 'network_name_example' # str | Name of an OpenStack network.

try: 
    # Return information about the ports of an OpenStack network.
    api_response = api_instance.openstack_rest_ports_network_name_get(network_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_ports_network_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_name** | **str**| Name of an OpenStack network. | 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openstack_rest_test_get**
> StdDefsJsondefinitionsnoschema openstack_rest_test_get()

Verify the user is authenticated and return openstack API version.

Verify the user is authenticated and return openstack API version.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()

try: 
    # Verify the user is authenticated and return openstack API version.
    api_response = api_instance.openstack_rest_test_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_test_get: %s\n" % e)
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

# **openstack_rest_volumes_get**
> StdDefsJsondefinitionsnoschema openstack_rest_volumes_get()

Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.

Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.NodeResourcesApi()

try: 
    # Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
    api_response = api_instance.openstack_rest_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeResourcesApi->openstack_rest_volumes_get: %s\n" % e)
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

