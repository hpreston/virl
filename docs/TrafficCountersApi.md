# virl.TrafficCountersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_counters_simulation_id_get**](TrafficCountersApi.md#simengine_rest_counters_simulation_id_get) | **GET** /simengine/rest/counters/{simulation_id} | List traffic on particular interfaces.


# **simengine_rest_counters_simulation_id_get**
> StdDefsJsondefinitionsnoschema simengine_rest_counters_simulation_id_get(simulation_id, nodes=nodes, networks=networks, interfaces=interfaces, type=type, step=step, count=count, datetype=datetype)

List traffic on particular interfaces.

List traffic on particular interfaces.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.TrafficCountersApi()
simulation_id = 'simulation_id_example' # str | simulation ID
nodes = ['nodes_example'] # list[str] | filter reported statistics by node (optional, defaults to all) (optional)
networks = ['networks_example'] # list[str] | filter reported statistics by network (optional, defaults to all) (optional)
interfaces = ['interfaces_example'] # list[str] | filter reported statistics by interface (optional, defaults to all) (optional)
type = 'type_example' # str | can be one of 'total' / 'rate' / 'avg' - type of report to generate (optional, defaults to 'total') (optional)
step = 56 # int | group values into groups of <step> (optional, defaults to 1) (optional)
count = 56 # int | number of values to return / consider in generating the stats. (optional, defaults to 1) (optional)
datetype = 'datetype_example' # str | ending point for the timeframe, in iso8601 format, e.g. 2016-04-15T12:47:00.000Z (optional)

try: 
    # List traffic on particular interfaces.
    api_response = api_instance.simengine_rest_counters_simulation_id_get(simulation_id, nodes=nodes, networks=networks, interfaces=interfaces, type=type, step=step, count=count, datetype=datetype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrafficCountersApi->simengine_rest_counters_simulation_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**| simulation ID | 
 **nodes** | [**list[str]**](str.md)| filter reported statistics by node (optional, defaults to all) | [optional] 
 **networks** | [**list[str]**](str.md)| filter reported statistics by network (optional, defaults to all) | [optional] 
 **interfaces** | [**list[str]**](str.md)| filter reported statistics by interface (optional, defaults to all) | [optional] 
 **type** | **str**| can be one of &#39;total&#39; / &#39;rate&#39; / &#39;avg&#39; - type of report to generate (optional, defaults to &#39;total&#39;) | [optional] 
 **step** | **int**| group values into groups of &lt;step&gt; (optional, defaults to 1) | [optional] 
 **count** | **int**| number of values to return / consider in generating the stats. (optional, defaults to 1) | [optional] 
 **datetype** | **str**| ending point for the timeframe, in iso8601 format, e.g. 2016-04-15T12:47:00.000Z | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

