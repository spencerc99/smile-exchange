import json
import os
from collections import defaultdict

# This stays static
DIR_PATH = '/System/Volumes/Data/Users/spencerchang/Library/Mobile Documents/iCloud~md~obsidian/Documents/obsidian-brain/daily/'
# This might changed if you have changed the tag
TAG = '#appreciations'
SEPARATOR = '::'
BULLET_CHARACTERS = ['-', '*', '+', '•']

files = os.listdir(DIR_PATH)

kindnesses = defaultdict(list)
IGNORE_LIST = [
    'wander prompts',
    '2022-05-10 arturo escobar pluriverse chat',
    'quiet confidence',
    'A Founders Guide to Options at the End of the World',
    'soothing-fire',
    'interact',
]

def find_persons(line):
    persons = []
    try: 
        start =line.index('[[')
        end= line.index(']]')

        maybe_person = line[start+2:end]

        if "|" in maybe_person:
            maybe_person = maybe_person.split("|")[0]
        
        if maybe_person not in IGNORE_LIST:
            persons.append(maybe_person.lower())

        return persons + find_persons(line[end+2:])
    except ValueError:
        return persons

# print(find_persons('* #friends/kindness-journal really admire the way [[jasmine wang]] fosters belonging and inclusivity and vibes'))


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
            persons = find_persons(line)
            for person in persons:
                # a regular expression that matches all possible bullet points at the start
                # and then removes them
                kindness = line.replace(f'{TAG} ', '')
                for bullet in BULLET_CHARACTERS:    
                    if kindness.startswith(bullet):
                        kindness = kindness.replace(bullet,'').strip()
                kindnesses[person].append(f'{file.replace(".md", "")}{SEPARATOR}{kindness}')

print (kindnesses.keys())
sorted_kindnesses = sorted_dict = dict(sorted(kindnesses.items()))

json_object = json.dumps(sorted_kindnesses, indent = 4) 
print(json_object)


# with open(DIR_PATH + '2022-11-18.md','r') as f:
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
