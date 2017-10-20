# virl.HealthCheckApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_health_delete**](HealthCheckApi.md#simengine_rest_health_delete) | **DELETE** /simengine/rest/health | Cancel running health check.
[**simengine_rest_health_get**](HealthCheckApi.md#simengine_rest_health_get) | **GET** /simengine/rest/health | Retrieve current health check status and results.
[**simengine_rest_health_put**](HealthCheckApi.md#simengine_rest_health_put) | **PUT** /simengine/rest/health | Run health check


# **simengine_rest_health_delete**
> StdDefsJsondefinitionsnoschema simengine_rest_health_delete()

Cancel running health check.

Cancel running health check

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.HealthCheckApi()

try: 
    # Cancel running health check.
    api_response = api_instance.simengine_rest_health_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthCheckApi->simengine_rest_health_delete: %s\n" % e)
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

# **simengine_rest_health_get**
> StdDefsJsondefinitionsnoschema simengine_rest_health_get()

Retrieve current health check status and results.

Retrieve current health check results and status

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.HealthCheckApi()

try: 
    # Retrieve current health check status and results.
    api_response = api_instance.simengine_rest_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthCheckApi->simengine_rest_health_get: %s\n" % e)
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

# **simengine_rest_health_put**
> StdDefsJsondefinitionsnoschema simengine_rest_health_put()

Run health check

Schedule a system and services health check.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.HealthCheckApi()

try: 
    # Run health check
    api_response = api_instance.simengine_rest_health_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthCheckApi->simengine_rest_health_put: %s\n" % e)
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

