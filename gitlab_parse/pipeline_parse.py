import json

from nr_nrdb import nrbd_write



def parse_pipeline_data(pipeline_data, license_key, account_id):
    
    #print(pipeline_data)
    
    nr_event={}
    nr_event['eventType'] = 'gitlabPipelineEvent'
    global_project_id = pipeline_data['project']['id']
    nr_event['git_project_id'] = global_project_id
    nr_pipeline_array = []
    
    for item in pipeline_data:
        if 'Object_attributes' == item:
            for o_item in pipeline_data['Object_attributes']:
                fix_project = 'object_attributes_detail_' + o_item
                nr_event[fix_project] = pipeline_data['Object_attributes'][o_item]
        elif 'project' == item:
    
            for p_item in pipeline_data['project']:
                fix_project = 'project_detail_' + p_item
                nr_event[fix_project] = pipeline_data['project'][p_item]
        elif 'commit' == item:
    
            for c_item in pipeline_data['commit']:
                fix_project = 'commit_detail_' + c_item
                nr_event[fix_project] = pipeline_data['commit'][c_item]
        elif 'builds' == item:
    
    
            for b_item in pipeline_data['builds']:
    
                nr_build_event = {}
                nr_build_event['eventType'] = 'gitlabPiplineBuildEvent'
                nr_build_event['git_project_id'] = global_project_id
                for b_detail in b_item:
                    nr_build_event[b_detail] = b_item[b_detail]
                nr_pipeline_array.append(nr_build_event)
        else:
            nr_event[item] = pipeline_data[item]
    
    
    
    #print(nr_event)
    nrbd_write.write_data(nr_event, license_key,account_id=account_id)
    #print(nr_pipeline_array)
    nrbd_write.write_data(nr_pipeline_array, license_key,account_id=account_id)