## Credit card fraud detection

### Development
This project contains jupter file where the source code is present where  Machine learning libraries are used to build a model for detecting the particular transaction is fraud or not. 
1. There is file called `transaction.csv` where sample of transactions containing all the details regarding transaction is fraud or not and other attributes of the transactions are provided.
2. All the steps like `Data Perception`, `Model Selection`, `Model Training`, `Model Evaluation`, `Model Tuning`, `Model deployment` has beed done 

### Deployment
This code takes the input as `transaction.csv` that contains transactions and generates `results.csv` as output with an extra column added named as `result`

Below are the steps to use this code.

1. Take the random number of transaction from `transactions.csv` file 
2. Drop the Class column
3. Save the list of transactions as `transactions.csv` or you can build your seperate `transactions.csv` using your own inputs for `v1,v2..`
4. Run the below code and you can find `results.csv` is generated in the same directory