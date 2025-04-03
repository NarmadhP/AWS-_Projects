we'll create a Lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

Description:
The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.


I have used boto3 for the python code, i have referred the boto3 documentation for creating the code,firstly i wrote down what was to be done and referred the documentation for the necessary steps
this can be used with cloudwatch and we can schedule it to run whenever we require
