import json
import os
import sys
from math import ceil

from progress_bar import ProgressBar
from glacier_wrapper import GlacierWrapper

PART_SIZE = 16777216


# read config
with open('config.json') as data_file:
    data = json.load(data_file)
account_id = data['account_id']
vault_name = data['vault_name']
directory = data['directory']
exts = data['ext']
log = open(vault_name + '.log', 'w')

os.system('grive -f -p ' + directory + '-l ' + vault_name + '_grivesync.log')
'''
# initialize Glacier wrapper
glacier = GlacierWrapper(account_id, PART_SIZE)
glacier.set_vault_name(vault_name)

# find all the files with the allowed extensions
filenames = [f for f in os.listdir(directory) if f.lower().endswith(tuple(exts))]
total = len(filenames)
ind = 1
for filename in filenames:
    file_path = directory + '/' + filename
    file_size = os.path.getsize(file_path)
    expected_part_count = ceil(file_size / PART_SIZE)
    print('(' + str(ind) + '/' + str(total) + ') ' + filename + ': ' + str(round(file_size/1024/1024)) + 'MB')

    upload_id = glacier.initiate_multipart_upload(file_path)
    with open(file_path, mode = 'rb') as archive:
        progress_bar = ProgressBar(expected_part_count)
        part_ind = 0
        content = archive.read(PART_SIZE)
        while True:
            progress_bar.advance()
            try:
                if glacier.upload_multipart_part(upload_id, part_ind, content):
                    archive_id = glacier.complete_multipart_upload(upload_id, archive)
                    print(filename + ',' + archive_id, file = log)
                    progress_bar.finish()
                    break;
                else:
                    content = archive.read(PART_SIZE)
                    part_ind += 1
            except TimeoutError as error:
                print(repr(error) + ' skip file')
                break;
            except KeyboardInterrupt:
                print('\nUser stopped!')
                sys.exit(0)
    archive.close()
    ind += 1

log.close()'''
