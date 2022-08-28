import json
from nr_nrdb import nrbd_write

def parse_release_data(release_data, license_key, account_id):
    # print(release_data)
    nr_event={}
    nr_event['eventType'] = 'gitlabreleaseEvent'
    global_project_id = release_data['project']['id']
    nr_event['git_project_id'] = global_project_id

    nr_commit_array = []

    for item in release_data:

        #Flatten the Project Detail

        if 'project' == item:

            for p_item in release_data['project']:
                fix_project = 'project_detail_' + p_item
                nr_event[fix_project] = release_data['project'][p_item]
        elif 'commit' == item:

            for p_item in release_data['commit']:
                fix_project = 'commit_detail_' + p_item
                nr_event[fix_project] = release_data['commit'][p_item]

        elif 'assets' == item:

            for p_item in release_data['assets']:
                if p_item == 'sources':

                    print(p_item)
                    source_array = []
                    for source_list in release_data['assets']['sources']:
                        print(source_list)
                        nr_event_sources = {}
                        nr_event_sources['git_project_id'] = global_project_id
                        nr_event_sources['eventType'] = 'gitlabReleaseSourcesEvent'
                        global_project_id = release_data['project']['id']
                        for source_detail in source_list:
                            nr_event_sources[source_detail] = source_list[source_detail]
                        source_array.append(nr_event_sources)





                else:
                    fix_project = 'asset_detail_' + p_item
                    nr_event[fix_project] = release_data['assets'][p_item]
                    print(nr_event[fix_project])
        else:
            nr_event[item] = release_data[item]


    #print(nr_event)
    nrbd_write.write_data(nr_event, license_key, account_id=account_id)
    print(source_array)
    nrbd_write.write_data(source_array, license_key, account_id=account_id)
    return {"result": "success"}