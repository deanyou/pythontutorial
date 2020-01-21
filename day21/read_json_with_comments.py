
import json5

jsonfile = open('syn_comments.json').read()

cfg = json5.loads(jsonfile)

print(cfg)
