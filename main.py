import copy

REPLACED = "the-text-has-been-replaced"

def create_flow(service_specs: list, deployment_specs: list, flow_uuid, text_to_replace):
    modified_deployment_specs = []

    for deployment_spec in deployment_specs:
        modified_deployment_spec = copy.deepcopy(deployment_spec)
        modified_deployment_spec['template']['metadata']['labels']['app'] = modified_deployment_spec['template']['metadata']['labels']['app'].replace(text_to_replace, REPLACED)
        modified_deployment_spec['selector']['matchLabels']['app'] = modified_deployment_spec['selector']['matchLabels']['app'].replace(text_to_replace, REPLACED)
        modified_deployment_spec['template']['spec']['containers'][0]['name'] = modified_deployment_spec['template']['spec']['containers'][0]['name'].replace(text_to_replace, REPLACED)
        
        modified_deployment_specs.append(modified_deployment_spec)

    config_map = {
        "original_text": text_to_replace
    }
  
    return {
        "deployment_specs": modified_deployment_specs,
        "config_map": config_map
    }

def delete_flow(config_map, flow_uuid):
    print(config_map["original_text"])
