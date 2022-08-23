import json
from nr_nrdb import nrbd_write

def parse_build_data(build_data, license_key, account_id):

    #print(build_data)

    nr_event={}
    nr_event['eventType'] = 'gitlabBuildEvent'
    global_project_id = build_data['project_id']
    nr_event['git_project_id'] = global_project_id
    nr_build_array = []

    for item in build_data:
        if 'runner' == item:

            try:
                for r_item in build_data['runner']:
                    fix_project = 'runner_detail_' + r_item
                    nr_event[fix_project] = build_data['runner'][r_item]
            except:
                pass
                nr_event['runner_detail_empty'] = 'empty'

        elif 'commit' == item:

            for c_item in build_data['commit']:
                fix_project = 'commit_detail_' + c_item
                nr_event[fix_project] = build_data['commit'][c_item]

        elif 'repository' == item:

            for r_item in build_data['repository']:
                fix_project = 'repository_detail_' + r_item
                nr_event[fix_project] = build_data['repository'][r_item]
        else:
            nr_event[item] = build_data[item]

    #print(nr_event)
    nrbd_write.write_data(nr_event, license_key,account_id=account_id)