## File upload to SWS S3

The sequence of actions:

1. First, we install `AWS CLI`:
```commandline
sudo apt install awscli
```
2. We need to adjust `AWS` configurations, type the following command from the terminal:
```commandline
aws configure
```
After pressing enter some config will be requested:
* access key ID - `AKIA476XMENJTLOCC4CE`
* secret access key - `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`
* default region name - `ap-northeast-3`
* output format - press `enter' itself, you don't need to enter anything

You don't need to enter anything in `output format', just press `enter'.

3. We can upload files through the terminal:
```commandline
aws s3 cp example.txt s3://my-bucket/
```
here:
* exmaple.txt - the file we want to upload will be `*.zip`.
* my-becket - the name of our becket is `traffic-low'

4. To view the files in `my-bucket`:
     ```commandline
     aws s3 ls s3://my-bucket/
     ```
    * my-becket - the name of our becket is `traffic-low'
