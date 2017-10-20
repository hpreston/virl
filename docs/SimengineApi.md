# virl.SimengineApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_calculate_requirements_post**](SimengineApi.md#simengine_rest_calculate_requirements_post) | **POST** /simengine/rest/calculate-requirements | Calculate hardware requirements
[**simengine_rest_events_simulation_get**](SimengineApi.md#simengine_rest_events_simulation_get) | **GET** /simengine/rest/events/{simulation} | Return a list of recent events recorded for a simulation
[**simengine_rest_export_simulation_get**](SimengineApi.md#simengine_rest_export_simulation_get) | **GET** /simengine/rest/export/{simulation} | Retrieve original VIRL XML Topology file
[**simengine_rest_launch_post**](SimengineApi.md#simengine_rest_launch_post) | **POST** /simengine/rest/launch | Create a new simulation
[**simengine_rest_list_get**](SimengineApi.md#simengine_rest_list_get) | **GET** /simengine/rest/list | Get a list of all simulations of this user, and the status of each simulation.
[**simengine_rest_nodes_simulation_get**](SimengineApi.md#simengine_rest_nodes_simulation_get) | **GET** /simengine/rest/nodes/{simulation} | List simulation nodes.
[**simengine_rest_serial_port_simulation_get**](SimengineApi.md#simengine_rest_serial_port_simulation_get) | **GET** /simengine/rest/serial_port/{simulation} | Return links to VM node serial ports.
[**simengine_rest_status_simulation_get**](SimengineApi.md#simengine_rest_status_simulation_get) | **GET** /simengine/rest/status/{simulation} | Return the status of a launched simulation
[**simengine_rest_stop_simulation_get**](SimengineApi.md#simengine_rest_stop_simulation_get) | **GET** /simengine/rest/stop/{simulation} | Schedule complete stop of a launched simulation
[**simengine_rest_tracking_post**](SimengineApi.md#simengine_rest_tracking_post) | **POST** /simengine/rest/tracking | Authorize a new simulation tracking channel
[**simengine_rest_tracking_tracking_id_delete**](SimengineApi.md#simengine_rest_tracking_tracking_id_delete) | **DELETE** /simengine/rest/tracking/{tracking_id} | Deauthorize a simulation tracking channel.
[**simengine_rest_tracking_tracking_id_get**](SimengineApi.md#simengine_rest_tracking_tracking_id_get) | **GET** /simengine/rest/tracking/{tracking_id} | Retrieve information on a simulation tracking channel
[**simengine_rest_update_simulation_start_get**](SimengineApi.md#simengine_rest_update_simulation_start_get) | **GET** /simengine/rest/update/{simulation}/start | Start simulation nodes previously stopped by simengine-update-stop
[**simengine_rest_update_simulation_stop_put**](SimengineApi.md#simengine_rest_update_simulation_stop_put) | **PUT** /simengine/rest/update/{simulation}/stop | Stop simulation nodes without tearing down the simulation
[**simengine_rest_updates_get**](SimengineApi.md#simengine_rest_updates_get) | **GET** /simengine/rest/updates | Get a list of all simulations of this user, and the status of each simulation.
[**simengine_rest_vnc_console_simulation_get**](SimengineApi.md#simengine_rest_vnc_console_simulation_get) | **GET** /simengine/rest/vnc_console/{simulation} | Return links to VM node VNC consoles


# **simengine_rest_calculate_requirements_post**
> StdDefsJsondefinitionsnoschema simengine_rest_calculate_requirements_post()

Calculate hardware requirements

Calculate hardware requirements for given topology.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()

try: 
    # Calculate hardware requirements
    api_response = api_instance.simengine_rest_calculate_requirements_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_calculate_requirements_post: %s\n" % e)
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

# **simengine_rest_events_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_events_simulation_get(simulation, since_id=since_id)

Return a list of recent events recorded for a simulation

Return a list of recent events recorded for a simulation. The response is a list of event dicts. If the request includes a sinceID, the response only contains events whose identifier is larger than the one set. It is safe to set sinceID = -1 if all events shall be retrieved. The current implementation returns exactly the same information as the `messages` key in the simengine-status response, albeit in a different format.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
since_id = 'null' # str | wait until simulation statusID changes from this value (optional) (default to null)

try: 
    # Return a list of recent events recorded for a simulation
    api_response = api_instance.simengine_rest_events_simulation_get(simulation, since_id=since_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_events_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **since_id** | **str**| wait until simulation statusID changes from this value | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_export_simulation_get**
> simengine_rest_export_simulation_get(simulation, updated=updated, startup_updated_configs=startup_updated_configs, download_configs=download_configs, running_configs=running_configs, startup_configs=startup_configs, nodes=nodes)

Retrieve original VIRL XML Topology file

Returns the original VIRL XML Topology file (or an equivalent serialization of it). Optionally, the dynamically-assigned IP addresses and prefixes are put into the file node and interface attributes and extension entries. Optionally, the running, startup, or startup-updated (by copying running config into startup config) configurations are retrieved over the serial ports of selected nodes that support it (i.e. all reference platforms). The downloaded configurations are put into extension entries which are the value of the options enabling the download; all three types are permitted for download at once, provided they end up in different extension entries. Downloads are only attempted on ACTIVE nodes if the subtype supports it. If some, but not all downloads fail, a 206 Partial Content is returned to indicate this condition. If all attempted downloads fail, a 500 response is generated.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
updated = null # bool | push information on dynamic IP addresses (optional) (default to null)
startup_updated_configs = 'null' # str | extension name for startup-updated config (optional) (default to null)
download_configs = 'null' # str | alias of startup-updated-configs (backwards compatibility) (optional) (default to null)
running_configs = 'null' # str | extension name for running config (optional) (default to null)
startup_configs = 'null' # str | extension name for startup config (optional) (default to null)
nodes = ['null'] # list[str] | select nodes to return by name or XPath expression - defaults to all nodes (optional) (default to null)

try: 
    # Retrieve original VIRL XML Topology file
    api_instance.simengine_rest_export_simulation_get(simulation, updated=updated, startup_updated_configs=startup_updated_configs, download_configs=download_configs, running_configs=running_configs, startup_configs=startup_configs, nodes=nodes)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_export_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **updated** | **bool**| push information on dynamic IP addresses | [optional] [default to null]
 **startup_updated_configs** | **str**| extension name for startup-updated config | [optional] [default to null]
 **download_configs** | **str**| alias of startup-updated-configs (backwards compatibility) | [optional] [default to null]
 **running_configs** | **str**| extension name for running config | [optional] [default to null]
 **startup_configs** | **str**| extension name for startup config | [optional] [default to null]
 **nodes** | [**list[str]**](str.md)| select nodes to return by name or XPath expression - defaults to all nodes | [optional] [default to null]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_launch_post**
> StdDefsJsondefinitionsnoschema simengine_rest_launch_post(session=session, file=file, mgmt_lxc=mgmt_lxc, mgmt_network=mgmt_network, mgmt_lxc_tcp_port=mgmt_lxc_tcp_port, version=version, wait=wait, expires=expires, mgmt_lxc_static_ip=mgmt_lxc_static_ip, static_serial_port_offset=static_serial_port_offset)

Create a new simulation

Create a new simulation and schedule its start. By default, the response is sent as soon as it is determined that the session launch is likely to succeed, but before any VM nodes are deployed. The user may therefore follow status updates on startup progress. To wait for VM nodes to deploy, set the 'wait' parameter. It is possible to change/add three parameters 'mgmt_...' to the simulation.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
session = 'null' # str | force exact name for the simulation (optional) (default to null)
file = 'session' # str | filename of the original .virl file - used as a base name (optional) (default to session)
mgmt_lxc = null # bool | overrides .virl file's management LXC settings e.g. `True` - run with management LXC (optional) (default to null)
mgmt_network = 'null' # str | override management network name (optional) (default to null)
mgmt_lxc_tcp_port = 56 # int | override management LXC management port number (optional)
version = 'null' # str | forces fail if versions mismatch (optional) (default to null)
wait = '0' # str | delay simulation start - time in minutes or datetime (optional) (default to 0)
expires = 'null' # str | simulation expiration - time in minutes or datetime (optional) (default to null)
mgmt_lxc_static_ip = 'null' # str | override management LXC's static IP (optional) (default to null)
static_serial_port_offset = 56 # int | override offset for static port mapping (optional)

try: 
    # Create a new simulation
    api_response = api_instance.simengine_rest_launch_post(session=session, file=file, mgmt_lxc=mgmt_lxc, mgmt_network=mgmt_network, mgmt_lxc_tcp_port=mgmt_lxc_tcp_port, version=version, wait=wait, expires=expires, mgmt_lxc_static_ip=mgmt_lxc_static_ip, static_serial_port_offset=static_serial_port_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_launch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| force exact name for the simulation | [optional] [default to null]
 **file** | **str**| filename of the original .virl file - used as a base name | [optional] [default to session]
 **mgmt_lxc** | **bool**| overrides .virl file&#39;s management LXC settings e.g. &#x60;True&#x60; - run with management LXC | [optional] [default to null]
 **mgmt_network** | **str**| override management network name | [optional] [default to null]
 **mgmt_lxc_tcp_port** | **int**| override management LXC management port number | [optional] 
 **version** | **str**| forces fail if versions mismatch | [optional] [default to null]
 **wait** | **str**| delay simulation start - time in minutes or datetime | [optional] [default to 0]
 **expires** | **str**| simulation expiration - time in minutes or datetime | [optional] [default to null]
 **mgmt_lxc_static_ip** | **str**| override management LXC&#39;s static IP | [optional] [default to null]
 **static_serial_port_offset** | **int**| override offset for static port mapping | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_list_get**
> StdDefsJsondefinitionsnoschema simengine_rest_list_get()

Get a list of all simulations of this user, and the status of each simulation.

Get a list of all simulations of this user, and the status of each simulation.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()

try: 
    # Get a list of all simulations of this user, and the status of each simulation.
    api_response = api_instance.simengine_rest_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_list_get: %s\n" % e)
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

# **simengine_rest_nodes_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_nodes_simulation_get(simulation, nodes=nodes)

List simulation nodes.

List simulation nodes.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | simulation ID
nodes = ['null'] # list[str] | select nodes for return by name or XPath, defaults to all nodes (optional) (default to null)

try: 
    # List simulation nodes.
    api_response = api_instance.simengine_rest_nodes_simulation_get(simulation, nodes=nodes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_nodes_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| simulation ID | 
 **nodes** | [**list[str]**](str.md)| select nodes for return by name or XPath, defaults to all nodes | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_serial_port_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_serial_port_simulation_get(simulation, nodes=nodes, mode=mode, port=port)

Return links to VM node serial ports.

Return links to VM node serial ports.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
nodes = ['null'] # list[str] | select nodes to return by name or XPath expression - defaults to all nodes (optional) (default to null)
mode = 'websocket' # str | serial port connection type (optional) (default to websocket)
port = 0 # int | serial port name or number (0 - console, 1 - monitor, 2 - aux) defaults to console (optional) (default to 0)

try: 
    # Return links to VM node serial ports.
    api_response = api_instance.simengine_rest_serial_port_simulation_get(simulation, nodes=nodes, mode=mode, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_serial_port_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **nodes** | [**list[str]**](str.md)| select nodes to return by name or XPath expression - defaults to all nodes | [optional] [default to null]
 **mode** | **str**| serial port connection type | [optional] [default to websocket]
 **port** | **int**| serial port name or number (0 - console, 1 - monitor, 2 - aux) defaults to console | [optional] [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_status_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_status_simulation_get(simulation, since_id=since_id, node_states=node_states)

Return the status of a launched simulation

Return the status of a launched simulation and user-visible messages. The response includes a statusID marker for the simulation. If the request includes a sinceID, the response waits until a status change occurs, or an internal timeout is exceeded to avoid blocking the server. If the simulation cannot be found (it was presumably deleted), a status is returned nonetheless, with the simulation status field being equal to `DONE`.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
since_id = 'null' # str | wait until simulation statusID changes from this value (optional) (default to null)
node_states = '0' # str | also return state nodes under the key `nodes` if the session exists and was not stopped (is not in state `DONE`) (optional) (default to 0)

try: 
    # Return the status of a launched simulation
    api_response = api_instance.simengine_rest_status_simulation_get(simulation, since_id=since_id, node_states=node_states)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_status_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **since_id** | **str**| wait until simulation statusID changes from this value | [optional] [default to null]
 **node_states** | **str**| also return state nodes under the key &#x60;nodes&#x60; if the session exists and was not stopped (is not in state &#x60;DONE&#x60;) | [optional] [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_stop_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_stop_simulation_get(simulation, wait=wait)

Schedule complete stop of a launched simulation

Schedule complete stop of a launched simulation. By default, the response is sent as soon as it is determined that the session stop is likely to succeed, but before any VM nodes are destroyed. The user may therefore follow status updates on teardown progress. To wait for the complete stop of the session, set the `wait` parameter.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
wait = 0 # int | number of seconds to wait for stopping the session (optional) (default to 0)

try: 
    # Schedule complete stop of a launched simulation
    api_response = api_instance.simengine_rest_stop_simulation_get(simulation, wait=wait)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_stop_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **wait** | **int**| number of seconds to wait for stopping the session | [optional] [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_tracking_post**
> StdDefsJsondefinitionsnoschema simengine_rest_tracking_post(session_id=session_id, topics=topics)

Authorize a new simulation tracking channel

Authorize a new simulation tracking channel

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
session_id = 'null' # str | filter future tracking messages by session ID (optional) (default to null)
topics = 'topics_example' # str | filter future tracking messages by their topics (optional)

try: 
    # Authorize a new simulation tracking channel
    api_response = api_instance.simengine_rest_tracking_post(session_id=session_id, topics=topics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_tracking_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| filter future tracking messages by session ID | [optional] [default to null]
 **topics** | **str**| filter future tracking messages by their topics | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_tracking_tracking_id_delete**
> StdDefsJsondefinitionsnoschema simengine_rest_tracking_tracking_id_delete(tracking_id)

Deauthorize a simulation tracking channel.

Deauthorize a simulation tracking channel.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
tracking_id = 'null' # str | ID of tracking (default to null)

try: 
    # Deauthorize a simulation tracking channel.
    api_response = api_instance.simengine_rest_tracking_tracking_id_delete(tracking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_tracking_tracking_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_id** | **str**| ID of tracking | [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_tracking_tracking_id_get**
> StdDefsJsondefinitionsnoschema simengine_rest_tracking_tracking_id_get(tracking_id)

Retrieve information on a simulation tracking channel

Retrieve information on a simulation tracking channel

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
tracking_id = 'null' # str | ID of tracking (default to null)

try: 
    # Retrieve information on a simulation tracking channel
    api_response = api_instance.simengine_rest_tracking_tracking_id_get(tracking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_tracking_tracking_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_id** | **str**| ID of tracking | [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_update_simulation_start_get**
> StdDefsJsondefinitionsnoschema simengine_rest_update_simulation_start_get(simulation, nodes=nodes, wait=wait)

Start simulation nodes previously stopped by simengine-update-stop

Start simulation nodes previously stopped by simengine-update-stop. Returns list of nodes which needed to start, as soon as all node deploy calls are made. The call does not wait until the nodes are deployed.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
nodes = ['null'] # list[str] | select nodes to start by name or XPath expression - defaults to all nodes (optional) (default to null)
wait = 0 # int | number of seconds to wait for nodes stop (optional) (default to 0)

try: 
    # Start simulation nodes previously stopped by simengine-update-stop
    api_response = api_instance.simengine_rest_update_simulation_start_get(simulation, nodes=nodes, wait=wait)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_update_simulation_start_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **nodes** | [**list[str]**](str.md)| select nodes to start by name or XPath expression - defaults to all nodes | [optional] [default to null]
 **wait** | **int**| number of seconds to wait for nodes stop | [optional] [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_update_simulation_stop_put**
> StdDefsJsondefinitionsnoschema simengine_rest_update_simulation_stop_put(simulation, nodes=nodes, wait=wait)

Stop simulation nodes without tearing down the simulation

Stop simulation nodes without tearing down the simulation. Returns list of nodes which needed to stop, as soon as all node destroy calls are made. The call does not wait until the nodes are torn down.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
nodes = ['null'] # list[str] | select nodes to stop by name or XPath expression - defaults to all nodes (optional) (default to null)
wait = 0 # int | number of seconds to wait for nodes stop (optional) (default to 0)

try: 
    # Stop simulation nodes without tearing down the simulation
    api_response = api_instance.simengine_rest_update_simulation_stop_put(simulation, nodes=nodes, wait=wait)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_update_simulation_stop_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **nodes** | [**list[str]**](str.md)| select nodes to stop by name or XPath expression - defaults to all nodes | [optional] [default to null]
 **wait** | **int**| number of seconds to wait for nodes stop | [optional] [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_updates_get**
> StdDefsJsondefinitionsnoschema simengine_rest_updates_get()

Get a list of all simulations of this user, and the status of each simulation.

Get information about current versions and available updates.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()

try: 
    # Get a list of all simulations of this user, and the status of each simulation.
    api_response = api_instance.simengine_rest_updates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_updates_get: %s\n" % e)
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

# **simengine_rest_vnc_console_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_vnc_console_simulation_get(simulation, node=node, mode=mode)

Return links to VM node VNC consoles

Return links to VM node VNC consoles. While each VM Node supports a VNC console, the reference platform routers cannot interact over this connection.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.SimengineApi()
simulation = 'simulation_example' # str | Simulation ID
node = ['null'] # list[str] | select nodes to return by name or XPath expression - defaults to all nodes (optional) (default to null)
mode = 'websocket' # str | serial port connection type (optional) (default to websocket)

try: 
    # Return links to VM node VNC consoles
    api_response = api_instance.simengine_rest_vnc_console_simulation_get(simulation, node=node, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimengineApi->simengine_rest_vnc_console_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **node** | [**list[str]**](str.md)| select nodes to return by name or XPath expression - defaults to all nodes | [optional] [default to null]
 **mode** | **str**| serial port connection type | [optional] [default to websocket]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

