# swagger_client.DevelopersApi

All URIs are relative to *https://virtserver.swaggerhub.com/NCATS_GNBR/GNBR_API/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_edge**](DevelopersApi.md#get_edge) | **GET** /queryEdge | Query for an edge
[**get_identifier**](DevelopersApi.md#get_identifier) | **GET** /findEntity | Find GNBR identifier
[**get_node_neighbors**](DevelopersApi.md#get_node_neighbors) | **GET** /getNodeNeighbors | Get all neighbors of a particular node
[**get_subgraph**](DevelopersApi.md#get_subgraph) | **GET** /getInducedSubgraph | Get a GNBR subgraph


# **get_edge**
> GnbrEdge get_edge(entity1, entity2)

Query for an edge

Query for edges connecting two entities within GNBR

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
entity1 = 'entity1_example' # str | GNBR-ID for first entity
entity2 = 'entity2_example' # str | GNBR-ID for second entity

try:
    # Query for an edge
    api_response = api_instance.get_edge(entity1, entity2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity1** | **str**| GNBR-ID for first entity | 
 **entity2** | **str**| GNBR-ID for second entity | 

### Return type

[**GnbrEdge**](GnbrEdge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identifier**
> IdMapping get_identifier(search_string, limit=limit)

Find GNBR identifier

Searches entities within GNBR for a matching ID, based on input string

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
search_string = 'search_string_example' # str | pass a search string to find matching identifiers
limit = 56 # int | maximum number of records to return (optional)

try:
    # Find GNBR identifier
    api_response = api_instance.get_identifier(search_string, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| pass a search string to find matching identifiers | 
 **limit** | **int**| maximum number of records to return | [optional] 

### Return type

[**IdMapping**](IdMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_neighbors**
> GnbrSubgraph get_node_neighbors(entity1)

Get all neighbors of a particular node

Query node to get all nodes connected by at least one edge to the input node within GNBR

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
entity1 = 'entity1_example' # str | GNBR-ID for first entity

try:
    # Get all neighbors of a particular node
    api_response = api_instance.get_node_neighbors(entity1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_node_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity1** | **str**| GNBR-ID for first entity | 

### Return type

[**GnbrSubgraph**](GnbrSubgraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subgraph**
> GnbrSubgraph get_subgraph(seed_nodes)

Get a GNBR subgraph

Query a list of nodes to get the GNBR subgraph induced by those nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
seed_nodes = ['seed_nodes_example'] # list[str] | gnbrIDs for subgraph

try:
    # Get a GNBR subgraph
    api_response = api_instance.get_subgraph(seed_nodes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_subgraph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seed_nodes** | [**list[str]**](str.md)| gnbrIDs for subgraph | 

### Return type

[**GnbrSubgraph**](GnbrSubgraph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

