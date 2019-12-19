# Amazon Connect - Tracking Order

## Create an Amazon Connect instance

* Create an instance of Amazon Connect
* Claim a **Toll free** number
* Creta a new contact flow called `tracking-order`, import the following file: [tracking-order](tracking-order) and **Save**.
* Edit your number and add the **tracking-order** contact flow.

## Create the database

* Create a DynamoDB table called `users` with the primary key `phone_number`.
* Create an new item with the following keys and values:
    * **phone_number** : `your-number`
    * **first_name** : `your-name`
* Create a DynamoDB table called `orders` with the primary key `order_id`.
    * **order_id** : `1234`
    * **status** : `En camino` 

## Create the logic

* Create a new Lambda function called `tracking-validate-user`, with runtime **Python 3.7** and select **Create a new role from AWS policy templates** with a role name `tracking-validate-user` and choose **Simple microservice permissions** and **Create function**.
* Add the environment variable `TABLE_NAME` with the value of `users`.
* Copy and paste the following code file: [tracking-validate-user.py](tracking-validate-user.py) and **Save**.
* Edit the lambda role and add `"dynamodb:Query"` permission.


* Create a new Lambda function called `tracking-check-order-status`, with runtime **Python 3.7** and select **Create a new role from AWS policy templates** with a role name `tracking-check-order-status` and choose **Simple microservice permissions** and **Create function**.
* Add the environment variable `TABLE_NAME` with the value of `orders`.
* Copy and paste the following code file: [tracking-check-order-status.py](tracking-check-order-status.py) and **Save**.
* Edit the lambda role and add `"dynamodb:Query"` permission.

## Complete Amazon Connect configuration

* Add **tracking-check-order-status** and **tracking-check-order-status** lambda functions to the instance of Amazon Connect.
* Edit the contact flow **tracking-order** by updating the **nvoke AWS Lambda function** components with the ARN of the lambdas created.