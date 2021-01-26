def clean_data(G_list):
    #irrelevent tags
    tags = ['id', 'horse', 'service', 'name:he', 'leaf_cycle', 'IS03166-2', 'name:ga', 'name:ja', 'operator:uk', 'motorcycle', 'car', 'dog', 'ISO3166-2', 'cycle_network', 'sport', 'capacity', 'icn_ref', 'name:tr', 'duration', 'colour', 'ons_code', 'source:ref:nuts:3', 'source:ons_code', 'council_style', 'name:fr', 'name:de', 'frequency', 'ref_group', 'addr:city', 'name:lt', 'name:gl', 'name:cy', 'capacity:disabled', 'short_name', 'name:ru', 'borough', 'council_name', 'leaf_type', 'notes', 'admin_level', 'fee', 'natural', 'park_ride', 'ref:gss', 'place', 'twitter', 'rowing', 'capacity:parent', 'name:en', 'name:cs', 'maxstay', 'contact:website', 'ref:nuts:3', 'leisure', 'boat', 'name:hr', 'name:it', 'name:es', 'boundary', 'covered', 'operator:nl', 'to', 'tt_ref', 'name:pt', 'name:sl', 'alt_name:de', 'office', 'landuse', 'distance', 'restriction', 'name:pl', 'type', 'name:zu', 'from', 'operator:fr', 'waterway', 'name:nl', 'operator:be', 'name:pl', 'wikidata', 'name:fi', 'network', 'wheelchair', 'source:building', 'name:be', 'parking', 'building', 'amenity', 'description', 'wikipedia', 'route', 'name:hu', 'url', 'water', 'source:ref:gss', 'source:ref:buts:3', 'website', 'footway', 'area', 'step_count', 'site', 'name:zh', 'name:gv', 'operator:lux', 'handrail', 'barrier', 'smoothness', 'towpath', 'not:name', 'vehicle', 'abutters', 'noname', 'ref:Chiltern_Society', 'source:name', 'prow_ref', 'source', 'cycleway', 'FIXME:nsl', 'fixme', 'bridge', 'est_width', 'layer', 'note', 'created_by', 'ncn', 'ncn_ref', 'direction', 'lcn_ref', 'junction', 'sidewalk', 'lcn', 'segregated', 'tracktype', 'cycleway:est_width', 'cycleway:left', 'width', 'surface', 'maxspeed:type', 'ref', 'maxspeed', 'bidrectional', 'motor_vehicle', 'access', 'cycleway:both', 'highway_authority_ref', 'alt_name', 'bicycle', 'construction_contract_name', 'designation', 'destination', 'highway', 'highways_england:area', 'bidirectional', 'lit', 'motorcar', 'old_ref', 'oneway', 'operator', 'source:destination', 'carriageway_ref', 'foot', 'int_ref', 'lanes', 'proposed:active_traffic_management', 'source:maxspeed']

    for val2, dict2 in G_list.items():
        for val3, dict3 in dict2.items():
            for tag in tags:
                #try to remove the irrelevent tag
                try:
                    del dict3[tag]
                except:
                    pass

    return G_list



