# CustomerUpdateFiscalEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from digitalfemsa.models.customer_update_fiscal_entities_request import CustomerUpdateFiscalEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerUpdateFiscalEntitiesRequest from a JSON string
customer_update_fiscal_entities_request_instance = CustomerUpdateFiscalEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerUpdateFiscalEntitiesRequest.to_json())

# convert the object into a dict
customer_update_fiscal_entities_request_dict = customer_update_fiscal_entities_request_instance.to_dict()
# create an instance of CustomerUpdateFiscalEntitiesRequest from a dict
customer_update_fiscal_entities_request_from_dict = CustomerUpdateFiscalEntitiesRequest.from_dict(customer_update_fiscal_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


