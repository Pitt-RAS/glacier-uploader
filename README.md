# glacier-uploader
A Python application to upload files to AWS Glacier

## Background
I wanted to backup my personal photos and videos to AWS Glacier but I didn't want to spend money on any software.

I have been learning Python for less than a month before this, and this is my first Python application.

## Dependency
* [Boto 3](https://boto3.readthedocs.org/en/latest/)

## Configuration
* Make sure AWS access key ID, access secret, and AWS default region are set up. Refer to [here](https://boto3.readthedocs.org/en/latest/guide/quickstart.html#configuration).
* Create a `config.json` file (or copy and rename `config-sample.json`). Insert AWS account ID, target vault name, and directory that needs to be backed up, as well as the file extensions that allowed.

## Usage
`$ python3 upload.py`

## Contribution
Again, I am super new to Python, and this is basically my first open-source project. It currently serves my need, but I want to keep improving it. Any issues and pull requests are welcome.

## License
MIT License
