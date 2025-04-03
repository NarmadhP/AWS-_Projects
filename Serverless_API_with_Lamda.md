we will be creating an API Gateway REST API with Lambda Integration

so the idea is that 
    client will hit the api which in turn will trigger our lambda function, which will create the response and the response will be forwaded to api and it will forward it to the client

firstly we will create
    1.API gateway
        -- using REST API
    2.Lamda Function
        --we will adding the api gateway as the trigger for the lambda function
    3. After creating these,we will create resouce and method in api gateway
        -- method will be pointed to lambda, from where the trigger will happen

    4.then we will deploy the api gateway
    5.after deployment, the lambda trigger will be updated to the api gateway
    6. we can test it and check the api endpoint.
