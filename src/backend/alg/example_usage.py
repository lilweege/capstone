import json
from v0_report_generation import report_generation

data = {'snippets': [
    "def hello_world(): print('Hello, world!')",
    "for i in range(10): print(i)",
    "def greet(name): print('Hello ' + name)",
    "for i in range(5): print(i)"
], 'threshold': 0.60}

data = json.dumps(data)


results = report_generation.generate(data)

print(results)

