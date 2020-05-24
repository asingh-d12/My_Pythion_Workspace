import json

import pprint

with open('temp_test.json') as a_json_file:
    all_data = json.load(a_json_file)

print(all_data['args']['player_response']['streamingData'].keys())

with open("o_file.json", 'w') as out:
    out.write(pprint.pformat(all_data['args']['player_response']['streamingData'], indent=1))
