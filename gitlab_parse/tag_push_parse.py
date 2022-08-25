import json

from nr_nrdb import nrbd_write


def parse_tag_push_data(tag_push_data, license_key, account_id):
    # print(tag_push_data)

    nr_event = {}
    nr_event['eventType'] = 'gitlabtag_pushEvent'
    global_project_id = tag_push_data['project']['id']
    nr_event['git_project_id'] = global_project_id
    nr_tag_push_array = []

    for item in tag_push_data:

        if 'project' == item:

            for p_item in tag_push_data['project']:
                fix_project = 'tag_push_project_detail_' + p_item
                nr_event[fix_project] = tag_push_data['project'][p_item]

        elif 'commit' == item:

            for c_item in tag_push_data['commit']:
                fix_project = 'tag_push_commit_detail_' + c_item
                nr_event[fix_project] = tag_push_data['commit'][c_item]

        else:
            nr_event[item] = tag_push_data[item]

    #print(nr_event)
    nrbd_write.write_data(nr_event, license_key, account_id=account_id)