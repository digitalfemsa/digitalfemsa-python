# TransferDestinationResponse

Method used to make the transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | **str** | Name of the account holder. | [optional] 
**account_number** | **str** | Account number of the bank account. | [optional] 
**bank** | **str** | Name of the bank. | [optional] 
**created_at** | **int** | Date and time of creation of the transfer. | [optional] 
**id** | **str** | Unique identifier of the transfer. | [optional] 
**object** | **str** | Object name, which is bank_transfer_payout_method. | [optional] 
**payee_id** | **str** | Unique identifier of the payee. | [optional] 
**type** | **str** | Type of the payee. | [optional] 

## Example

```python
from digitalfemsa.models.transfer_destination_response import TransferDestinationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDestinationResponse from a JSON string
transfer_destination_response_instance = TransferDestinationResponse.from_json(json)
# print the JSON string representation of the object
print(TransferDestinationResponse.to_json())

# convert the object into a dict
transfer_destination_response_dict = transfer_destination_response_instance.to_dict()
# create an instance of TransferDestinationResponse from a dict
transfer_destination_response_from_dict = TransferDestinationResponse.from_dict(transfer_destination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

