from pymongo import MongoClient
import json


#data = [{'Architecture': 'x86_64', 'CreationDate': '2023-07-22T22:07:16.000Z', 'ImageId': 'ami-00070a2af646b00d8', 'ImageLocation': '979382823631/bitnami-node-20.5.0-0-r01-linux-debian-11-x86_64-hvm-ebs-nami', 'ImageType': 'machine', 'Public': True, 'OwnerId': '979382823631', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-05cd245f735132dbb', 'VolumeSize': 10, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'VirtualName': 'ephemeral0'}, {'DeviceName': '/dev/sdc', 'VirtualName': 'ephemeral1'}, {'DeviceName': '/dev/sdd', 'VirtualName': 'ephemeral2'}, {'DeviceName': '/dev/sde', 'VirtualName': 'ephemeral3'}], 'Description': 'This image may not be the latest version available and might include security vulnerabilities. Please check the latest, up-to-date, available version at https://bitnami.com/stacks.', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'bitnami-node-20.5.0-0-r01-linux-debian-11-x86_64-hvm-ebs-nami', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'DeprecationTime': '2025-07-22T22:07:16.000Z'}, {'Architecture': 'arm64', 'CreationDate': '2024-05-06T00:14:08.000Z', 'ImageId': 'ami-000210c03635ab3ab', 'ImageLocation': '940213080334/elastio-amzn2023-arm64-1714953968', 'ImageType': 'machine', 'Public': True, 'OwnerId': '940213080334', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'Iops': 3000, 'SnapshotId': 'snap-0618d9150cc28464d', 'VolumeSize': 30, 'VolumeType': 'gp3', 'Throughput': 125, 'Encrypted': False}}], 'Description': 'Elastio Amazon Linux 2023 ARM64', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'elastio-amzn2023-arm64-1714953968', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'BootMode': 'uefi', 'DeprecationTime': '2026-05-06T00:14:08.000Z', 'ImdsSupport': 'v2.0'}, {'Architecture': 'x86_64', 'CreationDate': '2023-10-20T21:02:42.000Z', 'ImageId': 'ami-00070d439b967e320', 'ImageLocation': '979382823631/bitnami-mediawiki-1.40.1-5-r06-linux-debian-11-x86_64-hvm-ebs-nami', 'ImageType': 'machine', 'Public': True, 'OwnerId': '979382823631', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'State': 'available', 'BlockDeviceMappings': [{'DeviceName': '/dev/xvda', 'Ebs': {'DeleteOnTermination': True, 'SnapshotId': 'snap-0e67532524d081dd0', 'VolumeSize': 10, 'VolumeType': 'gp2', 'Encrypted': False}}, {'DeviceName': '/dev/sdb', 'VirtualName': 'ephemeral0'}, {'DeviceName': '/dev/sdc', 'VirtualName': 'ephemeral1'}, {'DeviceName': '/dev/sdd', 'VirtualName': 'ephemeral2'}, {'DeviceName': '/dev/sde', 'VirtualName': 'ephemeral3'}], 'Description': 'This image may not be the latest version available and might include security vulnerabilities. Please check the latest, up-to-date, available version at https://bitnami.com/stacks.', 'EnaSupport': True, 'Hypervisor': 'xen', 'Name': 'bitnami-mediawiki-1.40.1-5-r06-linux-debian-11-x86_64-hvm-ebs-nami', 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SriovNetSupport': 'simple', 'VirtualizationType': 'hvm', 'DeprecationTime': '2025-10-20T21:02:42.000Z'}]
with open("all.json","r") as f:
    data = f.read()

data = list(data)

print(type(data))
print(data)
#public_amis_list = json.loads(data)
# def merge_dicts_by_key(list_of_dicts, key):
#     merged_dict = {}
#     for d in list_of_dicts:
#         merged_dict[d[key]] = d
#     return merged_dict

# public_amis_dict = merge_dicts_by_key(data , 'ImageId')
# client = MongoClient('mongodb://localhost:27017/')
# db = client['AWS_AMI']  # Thay your_database_name bằng tên database thực tế của bạn
# collection = db["ami_pub"]

# try:
#     # Ensure public_amis is not empty
#     if not data:
#         raise ValueError("public_amis is empty")
#     # Insert data into MongoDB
#     collection.insert_many(data["Images"])
#     print("Data inserted successfully")
# except ValueError as ve:
#     print("Error:", ve)
# except Exception as e:
#     print("An error occurred:", e)
