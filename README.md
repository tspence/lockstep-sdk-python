# Lockstep API 
![PyPI](https://img.shields.io/pypi/v/lockstep-sdk)


A financial service API and platform for innovative accounting solutions providers.

### Who are we? 
Lockstep automates accounting workflows to improve your operational efficiency and cash flow. Accelerate payments through automated customer communications, enhanced collections activity management, and innovative forecasting and reporting.


# Getting Started

### Pip install the Lockstep API  
```bash
 path\\to\\project\\file: pip install lockstep-sdk
```

### Get Credentials

# TODO: WHERE SHOULD WE REDIRECT? 

{The SDK is all hosted here: https://api.sbx.lockstep.io/} ?? IS THIS OKAY?

### Pulling local environment variable with API key into program
```python
API_KEY = os.environ.get('INSERT_LOCAL_ENVIORNMENT_VARIABLE_HERE')
```

### Creating Client
```python
env = 'PASS_ENVIRONMENT_HERE'
client = LockstepApi(env)
client.with_api_key(apikey)

if not client:
    print("ISSUE WITH CLIENT, NO API KEY OR WRONG ENVIRONMENT")
else:
    print(f"CLIENT WAS CREATED SUCCESSFULLY: {client}")
    return client
```
You now have your API credentials and have successfully created your client

## Features (API Endpoints) 
- [Activities](https://developer.lockstep.io/reference/get_api-v1-activities-id)
- [ApiKeys](https://developer.lockstep.io/reference/get_api-v1-apikeys-id)
- [AppEnrollments](https://developer.lockstep.io/reference/get_api-v1-appenrollments-id)
- [Applications](https://developer.lockstep.io/reference/get_api-v1-applications-id)
- [Attachments](https://developer.lockstep.io/reference/get_api-v1-attachments-id)
- [Code Definitions](https://developer.lockstep.io/reference/get_api-v1-codedefinitions-id)
- [Companies](https://developer.lockstep.io/reference/get_api-v1-companies-id)
- [Contacts](https://developer.lockstep.io/reference/get_api-v1-contacts-id)
- [Countries](https://developer.lockstep.io/reference/get_api-v1-countries)
- [Credit Memo Applied](https://developer.lockstep.io/reference/get_api-v1-creditmemoapplied-id)
- [Currencies](https://developer.lockstep.io/reference/get_api-v1-currencies)
- [CustomFieldDefinitions](https://developer.lockstep.io/reference/get_api-v1-customfielddefinitions-id)
- [CustomFieldValues](https://developer.lockstep.io/reference/get_api-v1-customfieldvalues-definitionid-recordkey)
- [Definitions](https://developer.lockstep.io/reference/get_api-v1-definitions-countries)
- [Emails](https://developer.lockstep.io/reference/get_api-v1-emails-id)
- [Erps](https://developer.lockstep.io/reference/get_api-v1-erps)
- [InvoiceHistory](https://developer.lockstep.io/reference/get_api-v1-invoicehistory-id)
- [Invoices](https://developer.lockstep.io/reference/get_api-v1-invoices-id)
- [Leads](https://developer.lockstep.io/reference/post_api-v1-leads)
- [Migration](https://developer.lockstep.io/reference/post_api-v1-migration)
- [Notes](https://developer.lockstep.io/reference/get_api-v1-notes-id)
- [PaymentApplications](https://developer.lockstep.io/reference/get_api-v1-paymentapplications-id)
- [Payments](https://developer.lockstep.io/reference/get_api-v1-payments-id)
- [Provisioning](https://developer.lockstep.io/reference/post_api-v1-provisioning)
- [Reports](https://developer.lockstep.io/reference/get_api-v1-reports-cashflow)
- [States](https://developer.lockstep.io/reference/get_api-v1-states)
- [Status](https://developer.lockstep.io/reference/get_api-v1-status)
- [Sync](https://developer.lockstep.io/reference/post_api-v1-sync)
- [UserAccounts](https://developer.lockstep.io/reference/get_api-v1-useraccounts-id)
- [UserRoles](https://developer.lockstep.io/reference/get_api-v1-userroles-id)

## How to Use (Basic Usage)
This example will show you how to call an API, using the [Query Invoices API](https://developer.lockstep.io/reference/get_api-v1-invoices-query) to retrieve a collection of invoices. 

```python
env = 'sbx'
client = LockstepApi(env)
client.with_api_key({INSERT_API_KEY})

invoices = client.invoices.query_invoices(
            "invoiceDate",
            "Company",
            "invoiceDate asc",
            10,
            page_num)

print(invoices['records'])
```

## Sample Project 
Fetch Invoice Sample Python Project
{INSERT REFERENCE TO READ ME}




---- 
#### SAMPLE PROJECT BELOW MOVE TO EXAMPLE REPO

Many types of products examine invoices for a customer and provide feedback on them. A typical product might analyze incoming invoices and add metadata like a **credit score** for each invoice. This tutorial explains how to iterate through invoices and examine them. 

We use the [Query Invoices API](https://developer.lockstep.io/reference/get_api-v1-invoices-query) to retrieve a collection of invoices. To fetch a large number of invoices, we must use [filtering and pagination](https://developer.lockstep.io/docs/querying-with-searchlight). Here's how it works

## Step 1: Declaring and initializing LockstepApi
First,  you'll need to install LockstepAPI. You can do so in the terminal with 
```bash
pip install lockstep-sdk

```
Then you'll be able to start on your python file and utilize the lockstep API 
```python
import LockstepApi

# env can also be prd or your own url addres
env = 'sbx' 
client = LockstepApi(env)
client.with_api_key({INSERT_API_KEY})
```

### Check if you are connected to the API
```python
status_results = client.status.ping()
print(f"StatusResult: {status_results}")
```

## Step 2: Create API Query 

In this example, we will first query for invoices using the invoice date. We will fetch all invoices dated between Janurary 10, 2021 and May 10, 2021. We will specify a page size of 100 which gives us a small number of invoices in each query.

```python
invoices = client.invoices.query_invoices(
            "invoiceDate GT 2021-01-10 AND invoiceDate LT 2021-05-10", # filter query
            "Company", # includes extra fields
            "invoiceDate asc", # ordering
            100, # number of items per page
            1) # page number 
```

The results from this API call will list the first 100 invoices, since you specified the pagSize to be 100. The results will also include a `totalCount` field which tells you exactly how many records that matched your filter:

``` json
{
  "records": [
    {
      "groupKey": "1c043d8f-ce7e-4cf6-aa8e-a08b0220d327",
      "invoiceId": "23c57f74-b643-47bf-a82b-c90984b1fc1b",
      "companyId": "dab105d3-8fa3-4c4d-990a-c00cac91a064",
      "customerId": "453060e9-393e-4584-a5f6-31d8581c3969",
      "erpKey": "58784FB2-DD9F-4CAB-B672-575922DBFE3F",
      "purchaseOrderCode": "07E9A",
      "referenceCode": "DEMOI000000010",
      ...
    }
  ],
  "totalCount": 1919,
  "pageSize": 100
}
```
This is "Page Zero" of your results. You can then make additional API calls by specifying ?pageNumber=1 and so on.

## Step 3: Iterate through query results 

```python

        for record in invoices.json()['records']:
            print(f"Invoice: {record['invoiceId']}")
            print(f"Company name: {record['company']['companyName']}")
            print(f"Outstanding Balance: ${record['outstandingBalanceAmount']} \n")
            
```
Here we are accessing the records key value pairs. For every record we have record[Invoice ID], record[Company Name], and an record[outstanding balance amount] if any. 

## Step 3 Continued: Expected results

```bash
Invoice: 123456
Company Name: Your_Company_Name
Ooutstanding Balance: $ 0.00

```



Inspiration from: https://developer.lockstep.io/docs/fetch-invoices 
