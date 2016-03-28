import boto3
from botocore.utils import calculate_tree_hash
from botocore import exceptions

class GlacierWrapper:
    """A wrapper for Glacier commands
    """

    MAX_RETRY = 3

    def __init__(self, account_id, part_size = 67108864):
        self.account_id = account_id
        self.client = boto3.client('glacier')
        self.part_size = part_size

    def set_vault_name(self, vault_name):
        self.vault_name = vault_name

    def initiate_multipart_upload(self, filename):
        response = self.client.initiate_multipart_upload(
            vaultName = self.vault_name,
            archiveDescription = filename,
            partSize = str(self.part_size)
        )
        return response['uploadId']

    def upload_multipart_part(self, upload_id, part_ind, content):
        content_size = len(content)
        finish = False
        part_range = 'bytes ' + str(part_ind * self.part_size) + '-'
        if content_size < self.part_size: # last part
            part_range += str(part_ind * self.part_size + content_size - 1)
            finish = True
        else:
            part_range += str((part_ind + 1) * self.part_size - 1)
        part_range += '/*'
        retry = 0
        while retry < self.MAX_RETRY:
            try:
                response = self.client.upload_multipart_part(
                    vaultName = self.vault_name,
                    uploadId = upload_id,
                    range = part_range,
                    body = content
                )
            except exceptions.ClientError as e:
                print(e.response['Error']['Message'] + ' Retry...')
                retry += 1
                continue
            break
        if retry >= self.MAX_RETRY: # failed
            raise TimeoutError('Max number of retry.')
        return finish

    def complete_multipart_upload(self, upload_id, archive):
        size = archive.tell()
        archive.seek(0)
        checksum = calculate_tree_hash(archive)
        response = self.client.complete_multipart_upload(
            vaultName = self.vault_name,
            uploadId = upload_id,
            archiveSize = str(size),
            checksum = checksum
        )
        return response['archiveId']
