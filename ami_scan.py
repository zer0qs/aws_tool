import boto3
from pymongo import MongoClient
import json
from collections import Counter


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
        ]#, MaxResults= 6 |-> set if want to restrict number of AMIs to test
    )
    # Remove AWS Marketplace AMIs, remove Image owner of amazone and remove RootDevice type = instance store 
    for ami in response["Images"]:
        if ('ProductCodes' in ami) or ami.get('ImageOwnerAlias') == 'amazon' or ami.get('RootDeviceType') == 'instance-store':
            response["Images"].remove(ami)
    return response['Images']

# count_regions = []
def list_all_public_amis():
    """List all public AMIs in all AWS regions."""
    regions = list_all_regions()
    all_public_amis = []
    for region in regions:
        print(f"Fetching public AMIs in region: {region} - Total public AMIs found: ", end='')
        region_amis = get_all_public_amis_in_region(region)
        print(len(region_amis))
        # count_by_region = {region:len(region_amis)}
        # count_regions.append(count_by_region)
        all_public_amis.extend(region_amis)
    return all_public_amis

def count_amis_by_region():
    for region in count_regions:
        for key, value in region.items():
            print(f"{key}: {value}")

def remove_ownerID_more_than_50(amis):
    ownerid = [ami['OwnerId'] for ami in amis]
    owner_count = Counter(ownerid)
    owners_with_more_than_50_amis = {owner_id for owner_id, count in owner_count.items() if count >= 50}
    print('Found '+ str(len(owners_with_more_than_50_amis))+' OwnerID that have more than 50 AMIs')
    print('Removing AMIs of Owner who have more than 50 AMIs...')
    filtered_ami_list = [ami for ami in amis if ami['OwnerId'] not in owners_with_more_than_50_amis]

def insert_to_mongodb(data, collection_name='ami_data'):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['AWS_AMI']  # Thay your_database_name bằng tên database thực tế của bạn
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

if __name__ == "__main__":
    public_amis = list_all_public_amis()
    amis_after_filter = remove_ownerID_more_than_50(public_amis)
    print(f"Total public valid AMIs found: {len(amis_after_filter)}")
    insert_to_mongodb(amis_after_filter, collection_name='ami_data')
    
