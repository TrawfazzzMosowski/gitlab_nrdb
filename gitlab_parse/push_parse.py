import json
from nr_nrdb import nrbd_write

def parse_push_data(push_data, license_key, account_id):
    # print(push_data)
    nr_event={}
    nr_event['eventType'] = 'gitlabPushEvent'
    global_project_id = push_data['project_id']
    nr_event['git_project_id'] = global_project_id

    nr_commit_array = []

    for item in push_data:

        #Flatten the Project Detail

        if 'project' == item:

            for p_item in push_data['project']:
                fix_project = 'project_detail_' + p_item
                nr_event[fix_project] = push_data['project'][p_item]

        elif 'commits' == item:


            for c_item in push_data['commits']:
                nr_commit_event = {}
                nr_commit_event['eventType'] = 'gitlabPushCommitEvent'
                nr_commit_event['git_project_id'] = global_project_id
                for c_detail in c_item:
                    nr_commit_event[c_detail] = c_item[c_detail]
            nr_commit_array.append(nr_commit_event)


        elif 'repository' == item:

            for r_item in push_data['repository']:
                fix_project = 'repository_detail_' + r_item
                nr_event[fix_project] = push_data['project'][r_item]

        else:
            nr_event[item] = push_data[item]


    #print(nr_event)
    nrbd_write.write_data(nr_event, license_key, account_id=account_id)
    #print(nr_commit_array)
    nrbd_write.write_data(nr_commit_array, license_key, account_id=account_id)
    return {"result": "success"}