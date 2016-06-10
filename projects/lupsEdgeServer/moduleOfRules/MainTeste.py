from EngineRuleEdge import EngineRule

if __name__ == '__main__':
    engine = EngineRule()
    engine.run_rules(' "evento": "e", "id": 18,'+
      '"valor": 15 }',"313")
