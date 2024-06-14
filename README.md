
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
<img width="650" alt="image" src="https://github.com/zer0qs/aws_tool/assets/83699106/8f075ea8-df29-4d5d-941e-a45fdfac2116">


Check the data in MongoDB

<img width="1466" alt="image" src="https://github.com/zer0qs/aws_tool/assets/83699106/3991ca5d-bc7a-4ca4-b3c7-9eb550ccfd84">


