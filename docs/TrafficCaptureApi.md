# virl.TrafficCaptureApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_capture_simulation_delete**](TrafficCaptureApi.md#simengine_rest_capture_simulation_delete) | **DELETE** /simengine/rest/capture/{simulation} | Delete a traffic capture.
[**simengine_rest_capture_simulation_get**](TrafficCaptureApi.md#simengine_rest_capture_simulation_get) | **GET** /simengine/rest/capture/{simulation} | List available traffic captures, or fetch captured data.
[**simengine_rest_capture_simulation_post**](TrafficCaptureApi.md#simengine_rest_capture_simulation_post) | **POST** /simengine/rest/capture/{simulation} | Create a new traffic capture


# **simengine_rest_capture_simulation_delete**
> StdDefsJsondefinitionsnoschema simengine_rest_capture_simulation_delete(simulation, capture)

Delete a traffic capture.

Delete a traffic capture. Traffic captures will remain defined as long as the simulation exists, unless they are removed by this call, even if they are no longer, running due to reaching their limits, or if an error occurred. The captured data in offline captures is deleted as well.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficCaptureApi()
simulation = 'simulation_example' # str | Simulation ID
capture = 'capture_example' # str | select a specific capture

try: 
    # Delete a traffic capture.
    api_response = api_instance.simengine_rest_capture_simulation_delete(simulation, capture)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficCaptureApi->simengine_rest_capture_simulation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **capture** | **str**| select a specific capture | 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_capture_simulation_get**
> StdDefsJsondefinitionsnoschema simengine_rest_capture_simulation_get(simulation, capture=capture, accept=accept)

List available traffic captures, or fetch captured data.

List available traffic captures, or fetch captured data. Only offline captures can fetch their stored data, and can do so repeatedly, even if the traffic capture isn't running anymore.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficCaptureApi()
simulation = 'simulation_example' # str | Simulation ID
capture = 'null' # str | select a specific capture (optional) (default to null)
accept = 'null' # str | `application/vnd.tcpdump.pcap` download capture data (optional) (default to null)

try: 
    # List available traffic captures, or fetch captured data.
    api_response = api_instance.simengine_rest_capture_simulation_get(simulation, capture=capture, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficCaptureApi->simengine_rest_capture_simulation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **capture** | **str**| select a specific capture | [optional] [default to null]
 **accept** | **str**| &#x60;application/vnd.tcpdump.pcap&#x60; download capture data | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_capture_simulation_post**
> StdDefsJsondefinitionsnoschema simengine_rest_capture_simulation_post(simulation, node, interface, live_port=live_port, pcap_filter=pcap_filter, count=count, size=size, time=time)

Create a new traffic capture

Create a new traffic capture process attached to a running node interface. A traffic capture is either offline, collected to a file on the VIRL server, or live, exposing a TCP port on the VIRL server where the data can be collected. The capture process is subject to limits on the amounts of traffic that can be captures. If the client does not set these limits, the maximum allowed by server config is used.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficCaptureApi()
simulation = 'simulation_example' # str | Simulation ID
node = 'node_example' # str | select node where the traffic is captured by name
interface = 'interface_example' # str | select interface by ID or `management` keyword
live_port = 56 # int | Expose live capture on this port, 0 = automatic (optional)
pcap_filter = 'null' # str | filter captured traffic using a PCAP filter (optional) (default to null)
count = 56 # int | capture max `count` packets (optional)
size = 56 # int | capture max `size` MB of traffic (optional)
time = 56 # int | capture max `time` seconds of traffic (optional)

try: 
    # Create a new traffic capture
    api_response = api_instance.simengine_rest_capture_simulation_post(simulation, node, interface, live_port=live_port, pcap_filter=pcap_filter, count=count, size=size, time=time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficCaptureApi->simengine_rest_capture_simulation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| Simulation ID | 
 **node** | **str**| select node where the traffic is captured by name | 
 **interface** | **str**| select interface by ID or &#x60;management&#x60; keyword | 
 **live_port** | **int**| Expose live capture on this port, 0 &#x3D; automatic | [optional] 
 **pcap_filter** | **str**| filter captured traffic using a PCAP filter | [optional] [default to null]
 **count** | **int**| capture max &#x60;count&#x60; packets | [optional] 
 **size** | **int**| capture max &#x60;size&#x60; MB of traffic | [optional] 
 **time** | **int**| capture max &#x60;time&#x60; seconds of traffic | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

