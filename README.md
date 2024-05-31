
# MacOS

## Install Mongodb GUI 
```
brew tap mongodb/brew

brew install mongodb-community

brew services start mongodb-community

```
## Install  
```
pip install virtualenv

virtualenv venv

source venv/bin/activate

pip3 íntall -r requirement.txt

```
## Setup AWS configure

`aws configure `

- Using Access key and Secret key to configure aws work with python

## Set up  AWS account 
- Enable All AWS region to scan, by default, AWS enable 17 region
  
  Access [Manage Region](https://us-east-1.console.aws.amazon.com/billing/home?region=us-east-1#/account?AWS-Regions)

  Enable All region
  <img width="1323" alt="image" src="https://github.com/zer0qs/aws_tool/assets/83699106/49157ce4-22c2-4051-856c-fd741b641d45">

## Using 
It may take a long time to complete the scan if you want to test, set the `MaxResults` at line 34 to decrease the output data
```
python3 ami_scan.py
```
<img width="594" alt="image" src="https://github.com/zer0qs/aws_tool/assets/83699106/b9fc59bc-59bf-4347-a103-fc8c61c6516b">

Check the data in MongoDB

<img width="1717" alt="image" src="https://github.com/zer0qs/aws_tool/assets/83699106/a9a396be-e503-4b63-bb5e-61250fe50b6a">
