import boto3
# Import the boto3 library, used to interact with AWS services programmatically.

def lambda_handler(event, context):
    # This function serves as the entry point for the AWS Lambda execution.
    # 'event' contains data passed to the Lambda function during invocation.
    # 'context' provides runtime information about the Lambda function.

    ec2 = boto3.client('ec2')
    # Create a client object for the EC2 service. This allows interaction with EC2 resources like instances, volumes, and snapshots.

    # Fetch all EBS snapshots owned by the current AWS account.
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Retrieve details of all running EC2 instances in the account.
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()  # Initialize a set to store the IDs of running EC2 instances.

    # Iterate through all reservations to collect active instance IDs.
    # AWS groups EC2 instances into reservations for billing and operational purposes.
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            # Add each running EC2 instance's ID to the active_instance_ids set.
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot to evaluate whether it should be deleted.
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']  # Extract the unique ID of the snapshot.
        volume_id = snapshot.get('VolumeId')  # Extract the volume ID associated with the snapshot (if any).

        if not volume_id:
            # If no volume is associated with the snapshot, it's an orphan snapshot, so delete it.
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # If the snapshot is associated with a volume, check the volume's status.
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                # Fetch details of the volume associated with the snapshot.

                if not volume_response['Volumes'][0]['Attachments']:
                    # If the volume exists but is not attached to any EC2 instance, delete the snapshot.
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                # Handle the exception if the associated volume no longer exists in the account.
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # If the volume is deleted or not found, delete the snapshot as it's no longer relevant.
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
