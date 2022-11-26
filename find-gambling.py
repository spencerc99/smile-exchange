import json
import os
from collections import defaultdict

DIR_PATH = '/System/Volumes/Data/Users/spencerchang/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-brain/daily/'
TAG = '#me/gamble'
files = os.listdir(DIR_PATH)

gambles = []

for file in files:
    if os.path.isdir(DIR_PATH+file):
        continue
    with open(DIR_PATH + file,'r') as f:
        # print(f.readlines())
        # from pdb import set_trace
        # set_trace()
        filtered_lines = []
        for line in f.readlines():
            # print(line)
            if TAG in line:
                filtered_lines.append(line.strip()) 
        if filtered_lines:
            print('running through {}'.format(file))
        for line in filtered_lines:
            # persons = find_persons(line)
            # for person in persons:
                gambles.append(line.replace('* #me/gamble ', f'{file.replace(".md", "")}::'))

print (gambles)
json_object = json.dumps(gambles, indent = 4) 
print(json_object)


# with open(DIR_PATH + '2021-12-18.md','r') as f:
#     # print(f.readlines())
#     # from pdb import set_trace
#     # set_trace()
#     filtered_lines = []
#     for line in f.readlines():
#         # print(line)
#         if TAG in line:
#             filtered_lines.append(line.strip()) 
#     for line in filtered_lines:
#         persons = find_persons(line)
#         # print('hello')
#         for person in persons:
#             kindnesses[person].append(line)
