# virl
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.10
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import virl 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import virl
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**simengine_rest_admin_list_user_get**](docs/AdminApi.md#simengine_rest_admin_list_user_get) | **GET** /simengine/rest/admin-list/{user} | Get a list of all currently launched simulations
*AdminApi* | [**simengine_rest_admin_stop_user_simulation_put**](docs/AdminApi.md#simengine_rest_admin_stop_user_simulation_put) | **PUT** /simengine/rest/admin-stop/{user}/{simulation} | Stop a particular simulation or set of simulations
*AdminApi* | [**simengine_rest_admin_update_simulation_expiry_put**](docs/AdminApi.md#simengine_rest_admin_update_simulation_expiry_put) | **PUT** /simengine/rest/admin-update/{simulation}/expiry | Update simulation expiration
*AdminApi* | [**simengine_rest_jobs_get**](docs/AdminApi.md#simengine_rest_jobs_get) | **GET** /simengine/rest/jobs | Get current job processing information
*AdminApi* | [**simengine_rest_licensing_get**](docs/AdminApi.md#simengine_rest_licensing_get) | **GET** /simengine/rest/licensing | Get information on licensing
*AdminApi* | [**simengine_rest_systemlogs_get**](docs/AdminApi.md#simengine_rest_systemlogs_get) | **GET** /simengine/rest/systemlogs | Get a zip-file of all current logs
*AdminApi* | [**simengine_rest_test_get**](docs/AdminApi.md#simengine_rest_test_get) | **GET** /simengine/rest/test | List simengine API version and features, compatibility check
*AutonetkitApi* | [**ank_rest_process_post**](docs/AutonetkitApi.md#ank_rest_process_post) | **POST** /ank/rest/process | Process a VIRL XML Topology
*AutonetkitApi* | [**ank_rest_test_get**](docs/AutonetkitApi.md#ank_rest_test_get) | **GET** /ank/rest/test | Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
*CatalogApi* | [**root_get**](docs/CatalogApi.md#root_get) | **GET** / | List all supported URL rules and their associated methods
*HealthCheckApi* | [**simengine_rest_health_delete**](docs/HealthCheckApi.md#simengine_rest_health_delete) | **DELETE** /simengine/rest/health | Cancel running health check.
*HealthCheckApi* | [**simengine_rest_health_get**](docs/HealthCheckApi.md#simengine_rest_health_get) | **GET** /simengine/rest/health | Retrieve current health check status and results.
*HealthCheckApi* | [**simengine_rest_health_put**](docs/HealthCheckApi.md#simengine_rest_health_put) | **PUT** /simengine/rest/health | Run health check
*InterfacesApi* | [**simengine_rest_interfaces_simulation_get**](docs/InterfacesApi.md#simengine_rest_interfaces_simulation_get) | **GET** /simengine/rest/interfaces/{simulation} | List simulation interfaces.
*InterfacesApi* | [**simengine_rest_update_interfaces_simulation_put**](docs/InterfacesApi.md#simengine_rest_update_interfaces_simulation_put) | **PUT** /simengine/rest/update/interfaces/{simulation} | Update simulation nodes interfaces admin_state.
*LinksApi* | [**simengine_rest_link_simulation_id_get**](docs/LinksApi.md#simengine_rest_link_simulation_id_get) | **GET** /simengine/rest/link/{simulation_id} | Get link identifiers for selected simulation
*LinksApi* | [**simengine_rest_link_simulation_id_stringnode_id_iface_id_get**](docs/LinksApi.md#simengine_rest_link_simulation_id_stringnode_id_iface_id_get) | **GET** /simengine/rest/link/{simulation_id}/{string:node_id}/{iface_id} | Get info about a given link
*NodeResourcesApi* | [**openstack_rest_create_port_post**](docs/NodeResourcesApi.md#openstack_rest_create_port_post) | **POST** /openstack/rest/create-port | Create a port on an OpenStack network
*NodeResourcesApi* | [**openstack_rest_flavors_get**](docs/NodeResourcesApi.md#openstack_rest_flavors_get) | **GET** /openstack/rest/flavors | Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
*NodeResourcesApi* | [**openstack_rest_images_get**](docs/NodeResourcesApi.md#openstack_rest_images_get) | **GET** /openstack/rest/images | Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
*NodeResourcesApi* | [**openstack_rest_networks_get**](docs/NodeResourcesApi.md#openstack_rest_networks_get) | **GET** /openstack/rest/networks | Return information about OpenStack networks.
*NodeResourcesApi* | [**openstack_rest_ports_network_name_get**](docs/NodeResourcesApi.md#openstack_rest_ports_network_name_get) | **GET** /openstack/rest/ports/{network_name} | Return information about the ports of an OpenStack network.
*NodeResourcesApi* | [**openstack_rest_test_get**](docs/NodeResourcesApi.md#openstack_rest_test_get) | **GET** /openstack/rest/test | Verify the user is authenticated and return openstack API version.
*NodeResourcesApi* | [**openstack_rest_volumes_get**](docs/NodeResourcesApi.md#openstack_rest_volumes_get) | **GET** /openstack/rest/volumes | Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
*RosterApi* | [**roster_rest_get**](docs/RosterApi.md#roster_rest_get) | **GET** /roster/rest/ | Get GUI-related information on all user’s simulations
*RosterApi* | [**roster_rest_test_get**](docs/RosterApi.md#roster_rest_test_get) | **GET** /roster/rest/test | Verify the user is authenticated and return roster API version
*SimengineApi* | [**simengine_rest_calculate_requirements_post**](docs/SimengineApi.md#simengine_rest_calculate_requirements_post) | **POST** /simengine/rest/calculate-requirements | Calculate hardware requirements
*SimengineApi* | [**simengine_rest_events_simulation_get**](docs/SimengineApi.md#simengine_rest_events_simulation_get) | **GET** /simengine/rest/events/{simulation} | Return a list of recent events recorded for a simulation
*SimengineApi* | [**simengine_rest_export_simulation_get**](docs/SimengineApi.md#simengine_rest_export_simulation_get) | **GET** /simengine/rest/export/{simulation} | Retrieve original VIRL XML Topology file
*SimengineApi* | [**simengine_rest_launch_post**](docs/SimengineApi.md#simengine_rest_launch_post) | **POST** /simengine/rest/launch | Create a new simulation
*SimengineApi* | [**simengine_rest_list_get**](docs/SimengineApi.md#simengine_rest_list_get) | **GET** /simengine/rest/list | Get a list of all simulations of this user, and the status of each simulation.
*SimengineApi* | [**simengine_rest_nodes_simulation_get**](docs/SimengineApi.md#simengine_rest_nodes_simulation_get) | **GET** /simengine/rest/nodes/{simulation} | List simulation nodes.
*SimengineApi* | [**simengine_rest_serial_port_simulation_get**](docs/SimengineApi.md#simengine_rest_serial_port_simulation_get) | **GET** /simengine/rest/serial_port/{simulation} | Return links to VM node serial ports.
*SimengineApi* | [**simengine_rest_status_simulation_get**](docs/SimengineApi.md#simengine_rest_status_simulation_get) | **GET** /simengine/rest/status/{simulation} | Return the status of a launched simulation
*SimengineApi* | [**simengine_rest_stop_simulation_get**](docs/SimengineApi.md#simengine_rest_stop_simulation_get) | **GET** /simengine/rest/stop/{simulation} | Schedule complete stop of a launched simulation
*SimengineApi* | [**simengine_rest_tracking_post**](docs/SimengineApi.md#simengine_rest_tracking_post) | **POST** /simengine/rest/tracking | Authorize a new simulation tracking channel
*SimengineApi* | [**simengine_rest_tracking_tracking_id_delete**](docs/SimengineApi.md#simengine_rest_tracking_tracking_id_delete) | **DELETE** /simengine/rest/tracking/{tracking_id} | Deauthorize a simulation tracking channel.
*SimengineApi* | [**simengine_rest_tracking_tracking_id_get**](docs/SimengineApi.md#simengine_rest_tracking_tracking_id_get) | **GET** /simengine/rest/tracking/{tracking_id} | Retrieve information on a simulation tracking channel
*SimengineApi* | [**simengine_rest_update_simulation_start_get**](docs/SimengineApi.md#simengine_rest_update_simulation_start_get) | **GET** /simengine/rest/update/{simulation}/start | Start simulation nodes previously stopped by simengine-update-stop
*SimengineApi* | [**simengine_rest_update_simulation_stop_put**](docs/SimengineApi.md#simengine_rest_update_simulation_stop_put) | **PUT** /simengine/rest/update/{simulation}/stop | Stop simulation nodes without tearing down the simulation
*SimengineApi* | [**simengine_rest_updates_get**](docs/SimengineApi.md#simengine_rest_updates_get) | **GET** /simengine/rest/updates | Get a list of all simulations of this user, and the status of each simulation.
*SimengineApi* | [**simengine_rest_vnc_console_simulation_get**](docs/SimengineApi.md#simengine_rest_vnc_console_simulation_get) | **GET** /simengine/rest/vnc_console/{simulation} | Return links to VM node VNC consoles
*SnapshotApi* | [**simengine_rest_snapshot_simulation_node_post**](docs/SnapshotApi.md#simengine_rest_snapshot_simulation_node_post) | **POST** /simengine/rest/snapshot/{simulation}/{node} | Create snapshot of a node
*SubtypesApi* | [**simengine_rest_subtypes_get**](docs/SubtypesApi.md#simengine_rest_subtypes_get) | **GET** /simengine/rest/subtypes | List supported VM subtypes
*TrafficCaptureApi* | [**simengine_rest_capture_simulation_delete**](docs/TrafficCaptureApi.md#simengine_rest_capture_simulation_delete) | **DELETE** /simengine/rest/capture/{simulation} | Delete a traffic capture.
*TrafficCaptureApi* | [**simengine_rest_capture_simulation_get**](docs/TrafficCaptureApi.md#simengine_rest_capture_simulation_get) | **GET** /simengine/rest/capture/{simulation} | List available traffic captures, or fetch captured data.
*TrafficCaptureApi* | [**simengine_rest_capture_simulation_post**](docs/TrafficCaptureApi.md#simengine_rest_capture_simulation_post) | **POST** /simengine/rest/capture/{simulation} | Create a new traffic capture
*TrafficControlApi* | [**simengine_rest_shaping_interfaces_simulation_id_delete**](docs/TrafficControlApi.md#simengine_rest_shaping_interfaces_simulation_id_delete) | **DELETE** /simengine/rest/shaping-interfaces/{simulation_id} | Delete interface-level traffic control settings for all links in simulation
*TrafficControlApi* | [**simengine_rest_shaping_interfaces_simulation_id_get**](docs/TrafficControlApi.md#simengine_rest_shaping_interfaces_simulation_id_get) | **GET** /simengine/rest/shaping-interfaces/{simulation_id} | List interface-level traffic control settings
*TrafficControlApi* | [**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get**](docs/TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get) | **GET** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id} | List interface-level traffic control settings for a given node in simulation
*TrafficControlApi* | [**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get**](docs/TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get) | **GET** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id}/{string:iface_id} | List interface-level traffic control setting for a given interface of node in simulation
*TrafficControlApi* | [**simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put**](docs/TrafficControlApi.md#simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put) | **PUT** /simengine/rest/shaping-interfaces/{string:simulation_id}/{string:node_id}/{string:iface_id} | Set interface-level traffic control settings for particular interface
*TrafficControlApi* | [**simengine_rest_shaping_simulation_id_delete**](docs/TrafficControlApi.md#simengine_rest_shaping_simulation_id_delete) | **DELETE** /simengine/rest/shaping/{simulation_id} | Delete link-level traffic control settings for all links in simulation
*TrafficControlApi* | [**simengine_rest_shaping_simulation_id_get**](docs/TrafficControlApi.md#simengine_rest_shaping_simulation_id_get) | **GET** /simengine/rest/shaping/{simulation_id} | List link-level traffic control settings
*TrafficControlApi* | [**simengine_rest_shaping_simulation_id_link_id_delete**](docs/TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_delete) | **DELETE** /simengine/rest/shaping/{simulation_id}/{link_id} | Delete link-level traffic control settings for particular link
*TrafficControlApi* | [**simengine_rest_shaping_simulation_id_link_id_get**](docs/TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_get) | **GET** /simengine/rest/shaping/{simulation_id}/{link_id} | List link-level traffic control settings for a given link
*TrafficControlApi* | [**simengine_rest_shaping_simulation_id_link_id_put**](docs/TrafficControlApi.md#simengine_rest_shaping_simulation_id_link_id_put) | **PUT** /simengine/rest/shaping/{simulation_id}/{link_id} | Set link-level traffic control settings for particular link
*TrafficCountersApi* | [**simengine_rest_counters_simulation_id_get**](docs/TrafficCountersApi.md#simengine_rest_counters_simulation_id_get) | **GET** /simengine/rest/counters/{simulation_id} | List traffic on particular interfaces.
*VolumeApi* | [**simengine_rest_simulation_node_attach_volume_get**](docs/VolumeApi.md#simengine_rest_simulation_node_attach_volume_get) | **GET** /simengine/rest/{simulation}/{node}/attach/{volume} | Attach volume to a running node.
*VolumeApi* | [**simengine_rest_simulation_node_detach_volume_get**](docs/VolumeApi.md#simengine_rest_simulation_node_detach_volume_get) | **GET** /simengine/rest/{simulation}/{node}/detach/{volume} | Detach volume from a running node.


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author



