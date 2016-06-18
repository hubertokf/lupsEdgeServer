from EngineRuleEdge import EngineRule
import json
if __name__ == '__main__':
    a = '[ {"conditions": { "all": [ { "name": "getNumber","operator": "greater_than","value": 5},'
    a = a +  '{ "name": "getNumber","operator": "less_than", "value": 99 }]},'
    a = a + '"actions": [ { "name": "test_post_Event", "params": {"inf": "funf"}}]},'
    a = a +  '{"conditions": { "all": [ { "name": "getNumber", "operator": "greater_than", "value": 99 } ] },'
    a = a +  '"actions": [ { "name": "test_post_Event",  "params": {"inf": "deuruim"} } ]}]'

    j = json.loads(a)

    engine = EngineRule()
    engine.run_rules('{ "evento": "e", "id": 18,'+
      '"valor": 100 }')
