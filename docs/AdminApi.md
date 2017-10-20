# virl.AdminApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simengine_rest_admin_list_user_get**](AdminApi.md#simengine_rest_admin_list_user_get) | **GET** /simengine/rest/admin-list/{user} | Get a list of all currently launched simulations
[**simengine_rest_admin_stop_user_simulation_put**](AdminApi.md#simengine_rest_admin_stop_user_simulation_put) | **PUT** /simengine/rest/admin-stop/{user}/{simulation} | Stop a particular simulation or set of simulations
[**simengine_rest_admin_update_simulation_expiry_put**](AdminApi.md#simengine_rest_admin_update_simulation_expiry_put) | **PUT** /simengine/rest/admin-update/{simulation}/expiry | Update simulation expiration
[**simengine_rest_jobs_get**](AdminApi.md#simengine_rest_jobs_get) | **GET** /simengine/rest/jobs | Get current job processing information
[**simengine_rest_licensing_get**](AdminApi.md#simengine_rest_licensing_get) | **GET** /simengine/rest/licensing | Get information on licensing
[**simengine_rest_systemlogs_get**](AdminApi.md#simengine_rest_systemlogs_get) | **GET** /simengine/rest/systemlogs | Get a zip-file of all current logs
[**simengine_rest_test_get**](AdminApi.md#simengine_rest_test_get) | **GET** /simengine/rest/test | List simengine API version and features, compatibility check


# **simengine_rest_admin_list_user_get**
> StdDefsJsondefinitionsnoschema simengine_rest_admin_list_user_get(user)

Get a list of all currently launched simulations

Get a list of all currently launched simulations, optionally filtered by `user`. This call is mainly intended for administrative monitoring of STD. An admin user is required to perform this call.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()
user = 'user_example' # str | username or keyword `__all__`

try: 
    # Get a list of all currently launched simulations
    api_response = api_instance.simengine_rest_admin_list_user_get(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_admin_list_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| username or keyword &#x60;__all__&#x60; | 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_admin_stop_user_simulation_put**
> StdDefsJsondefinitionsnoschema simengine_rest_admin_stop_user_simulation_put(user, simulation, wait)

Stop a particular simulation or set of simulations

Stop a particular simulation or all simulations of one / all users. This call is mainly intended for administrative cleanup of STD. An admin user is required to perform this call. `__all__` can be used instead of simulation ID or username.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()
user = 'user_example' # str | username or keyword `__all__`
simulation = 'simulation_example' # str | simulation id or keyword `__all__`
wait = '0' # str | number of seconds to wait for session stop, default = `0` (default to 0)

try: 
    # Stop a particular simulation or set of simulations
    api_response = api_instance.simengine_rest_admin_stop_user_simulation_put(user, simulation, wait)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_admin_stop_user_simulation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| username or keyword &#x60;__all__&#x60; | 
 **simulation** | **str**| simulation id or keyword &#x60;__all__&#x60; | 
 **wait** | **str**| number of seconds to wait for session stop, default &#x3D; &#x60;0&#x60; | [default to 0]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_admin_update_simulation_expiry_put**
> StdDefsJsondefinitionsnoschema simengine_rest_admin_update_simulation_expiry_put(simulation, user, expires=expires)

Update simulation expiration

Get a list of all currently launched simulations, optionally filtered by `user`. This call is mainly intended for administrative monitoring of STD. An admin user is required to perform this call.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()
simulation = 'simulation_example' # str | simulation ID
user = 'user_example' # str | name of the user that launched the simulation
expires = 'expires_example' # str | number of minutes or datetime when the simulation will be automatically terminated. If not given, expiration will be reset (optional)

try: 
    # Update simulation expiration
    api_response = api_instance.simengine_rest_admin_update_simulation_expiry_put(simulation, user, expires=expires)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_admin_update_simulation_expiry_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation** | **str**| simulation ID | 
 **user** | **str**| name of the user that launched the simulation | 
 **expires** | **str**| number of minutes or datetime when the simulation will be automatically terminated. If not given, expiration will be reset | [optional] 

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_jobs_get**
> StdDefsJsondefinitionsnoschema simengine_rest_jobs_get()

Get current job processing information

Get current job processing information. Stub implemented for compatibility with other VMMaestro backends. Returns an empty list

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()

try: 
    # Get current job processing information
    api_response = api_instance.simengine_rest_jobs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_jobs_get: %s\n" % e)
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

# **simengine_rest_licensing_get**
> StdDefsJsondefinitionsnoschema simengine_rest_licensing_get()

Get information on licensing

Get information on licensing. This call is mainly intended for the GUI at topology launch time.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()

try: 
    # Get information on licensing
    api_response = api_instance.simengine_rest_licensing_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_licensing_get: %s\n" % e)
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

# **simengine_rest_systemlogs_get**
> simengine_rest_systemlogs_get()

Get a zip-file of all current logs

Get a zip-file of all current logs, from STD, UWM and lmgrd. This call is mainly intended for assisting troubleshooting. An admin user is required to perform this call.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()

try: 
    # Get a zip-file of all current logs
    api_instance.simengine_rest_systemlogs_get()
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_systemlogs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simengine_rest_test_get**
> StdDefsJsondefinitionsnoschema simengine_rest_test_get(error_unknown=error_unknown)

List simengine API version and features, compatibility check

Verify the user is authenticated and return simengine API version. Also checks for client compatibility if provided against internal config. The client takes the form ClientName-ClientVersion (split on first dash). If the client is known to STD, returns a bool (true or false), if client info is not provided, or unknown, return null. Also displays supported features list.

### Example 
```python
from __future__ import print_function
import time
import virl
from virl.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = virl.AdminApi()
error_unknown = 'null' # str | Client identification for compatibility check, in format client-version, will return `{  \"client-compatible\": true|false|null }` instead. `null` indicates an unknown client (optional) (default to null)

try: 
    # List simengine API version and features, compatibility check
    api_response = api_instance.simengine_rest_test_get(error_unknown=error_unknown)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->simengine_rest_test_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_unknown** | **str**| Client identification for compatibility check, in format client-version, will return &#x60;{  \&quot;client-compatible\&quot;: true|false|null }&#x60; instead. &#x60;null&#x60; indicates an unknown client | [optional] [default to null]

### Return type

[**StdDefsJsondefinitionsnoschema**](StdDefsJsondefinitionsnoschema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

