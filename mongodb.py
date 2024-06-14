import boto3
from pymongo import MongoClient
import json
from collections import Counter
import os


def list_all_regions():
    """Get all AWS regions."""
    ec2_client = boto3.client('ec2')
    regions = ec2_client.describe_regions()
    return [region['RegionName'] for region in regions['Regions']]

def get_all_public_amis_in_region(region_name):
    """Get all public AMIs in a specific region."""
    ec2_client = boto3.client('ec2', region_name=region_name)
    response = ec2_client.describe_images(
        Filters=[
            {
                'Name': 'is-public',
                'Values': ['true']
            }
        ], MaxResults= 10 #|-> set if want to restrict number of AMIs to test
    )
    # Remove AWS Marketplace AMIs, remove Image owner of amazone and remove RootDevice type = instance store 
    for ami in response["Images"][:]:
        if ('ProductCodes' in ami) or ami.get('ImageOwnerAlias') == 'amazon' or ami.get('RootDeviceType') == 'instance-store':
            response["Images"].remove(ami)
    return response['Images']

# count_regions = []
def list_all_public_amis():
    """List all public AMIs in all AWS regions."""
    regions = list_all_regions()
    all_public_amis = []
    x_count = 0
    count=0
    for region in regions:
        print(f"Fetching public AMIs in region: {region} - Total public AMIs found: ", end='')
        
        region_amis = get_all_public_amis_in_region(region)
        
        region_amis = remove_ownerID_more_than_50(region_amis)
        test = [{'Architecture': 'x86_64', 'CreationDate': '2023-05-25T20:36:48.000Z', 'ImageId': 'ami-000012c9eb58c8665', 'ImageLocation': '979382823631/bitnami-wordpressmultisite-6.2.2-5-r05-linux-debian-11-x86_64-hvm-ebs-nami', 'ImageType': 'machine', 'Public': True, 'OwnerId': '979382823631', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-03abc0fa5f48d8137', 'VolumeSize': 2000, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'VirtualName': 'ephemeral0'}, {'DeviceName': '/dev/sdc', 'VirtualName': 'ephemeral1'}, {'DeviceName': '/dev/sdd', 'VirtualName': 'ephemeral2'}, {'DeviceName': '/dev/sde', 'VirtualName': 'ephemeral3'}], 'Description': 'This image may not be the latest version available and might include security vulnerabilities. Please check the latest, up-to-date, available version at https://bitnami.com/stacks.', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'bitnami-wordpressmultisite-6.2.2-5-r05-linux-debian-11-x86_64-hvm-ebs-nami', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'DeprecationTime': '2025-05-25T20:36:48.000Z'}, {'Architecture': 'x86_64', 'CreationDate': '2023-06-08T05:06:21.000Z', 'ImageId': 'ami-0000b16040ac7c8fa', 'ImageLocation': '979382823631/bitnami-meanstack-5.0.18-6-r09-linux-debian-11-x86_64-hvm-ebs-nami', 'ImageType': 'machine', 'Public': True, 'OwnerId': '979382823631', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-09a0e09eb8c66e83e', 'VolumeSize': 1000, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'VirtualName': 'ephemeral0'}, {'DeviceName': '/dev/sdc', 'VirtualName': 'ephemeral1'}, {'DeviceName': '/dev/sdd', 'VirtualName': 'ephemeral2'}, {'DeviceName': '/dev/sde', 'VirtualName': 'ephemeral3'}], 'Description': 'This image may not be the latest version available and might include security vulnerabilities. Please check the latest, up-to-date, available version at https://bitnami.com/stacks.', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'bitnami-meanstack-5.0.18-6-r09-linux-debian-11-x86_64-hvm-ebs-nami', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'DeprecationTime': '2025-06-08T05:06:21.000Z'}, {'Architecture': 'x86_64', 'CreationDate': '2023-04-12T05:39:15.000Z', 'ImageId': 'ami-00009703aa7c0ca31', 'ImageLocation': '979382823631/bitnami-wordpress-6.2.0-6-r05-linux-debian-11-x86_64-hvm-ebs-nami', 'ImageType': 'machine', 'Public': True, 'OwnerId': '979382823631', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-0ce3b8ab7cf15536f', 'VolumeSize': 10, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'VirtualName': 'ephemeral0'}, {'DeviceName': '/dev/sdc', 'VirtualName': 'ephemeral1'}, {'DeviceName': '/dev/sdd', 'VirtualName': 'ephemeral2'}, {'DeviceName': '/dev/sde', 'VirtualName': 'ephemeral3'}], 'Description': 'This image may not be the latest version available and might include security vulnerabilities. Please check the latest, up-to-date, available version at https://bitnami.com/stacks.', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'bitnami-wordpress-6.2.0-6-r05-linux-debian-11-x86_64-hvm-ebs-nami', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'DeprecationTime': '2025-04-12T05:39:15.000Z'}]
        region_amis = remove_big_volumn_size(test)
        print(len(region_amis))
        x_count += len(region_amis)
        all_region_amis= {}
        all_region_amis[region] = list_ami_id(region_amis)
        all_public_amis.append(all_region_amis)
        if count ==1:
            break
        count +=1
    return all_public_amis,x_count
def list_ami_id(amis):
    ami_ids=[]
    for ami in amis:
        ami_ids.append(ami['ImageId'])
    return ami_ids
def remove_ownerID_more_than_50(amis):
    ownerid = [ami['OwnerId'] for ami in amis]
    owner_count = Counter(ownerid)
    owners_with_more_than_50_amis = {owner_id for owner_id, count in owner_count.items() if count >= 50}
    filtered_ami_list = [ami for ami in amis if ami['OwnerId'] not in owners_with_more_than_50_amis]
    return filtered_ami_list
def remove_big_volumn_size(amis):
    if amis:
        for ami in amis[:]:
            bdm = ami['BlockDeviceMappings']
            ebs_items = [x['Ebs'] for x in bdm if 'Ebs' in x.keys()]
            ebs_items = [x for x in ebs_items if 'SnapshotId' in x.keys()]
            big_snapshots = [x for x in ebs_items if x['VolumeSize'] > 200]
            if len(ebs_items) > 3 or len(big_snapshots) > 0:
                amis.remove(ami)
    return amis

def insert_to_mongodb(data, collection_name='ami_data'):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AWS_AMI']
    collection = db[collection_name]
    try:
        # Ensure public_amis is not empty
        if not data:
            raise ValueError("public_amis is empty")
        # Insert data into MongoDB
        collection.insert_many(data)
        print("Data inserted successfully")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

def get_amis(scan):
    ami_dict = {}
    for region_data in scan:
        for region, amis in region_data.items():
            if region not in ami_dict:
                ami_dict[region] = set()
            ami_dict[region].update(amis)
    return ami_dict

def find_new_amis(previous_scan, current_scan):
    previous_amis = get_amis(previous_scan)
    current_amis = get_amis(current_scan)
    
    new_amis = {}
    for region in current_amis:
        if region in previous_amis:
            new_amis[region] = list(current_amis[region] - previous_amis[region])
        else:
            new_amis[region] = list(current_amis[region])
    
    # Filter out empty entries
    new_amis = {region: amis for region, amis in new_amis.items() if amis}
    count_new = 0
    for region in new_amis:
        count_new +=len(region)
    return new_amis,count_new

if __name__ == "__main__":
    public_amis, x_count = list_all_public_amis()
    print(f"Total public valid AMIs found: {x_count}")
    print(public_amis)
    # if os.path.isfile("old_ami.json"):
    #     with open("old_ami.json", "r") as file:
    #         previous_scan = json.load(file)
    #     # Find new AMIs
    #     new_amis,count_new = find_new_amis(previous_scan, public_amis)
    #     print("Found: "+str(count_new)+" new AMIs in current scan, it is stored in new_ami.json")
    #     if new_amis:
    #         with open("old_ami.json", "w") as file:
    #             json.dump(public_amis, file, indent=4)
    #         with open("new_ami.json", "w") as file:
    #             json.dump(new_amis, file, indent=4)
    # else:
    #     with open("old_ami.json", "w") as file:
    #         json.dump(public_amis, file, indent=4)
    

    #insert_to_mongodb(public_amis, collection_name='ami_data')


 

    
