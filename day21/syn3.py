
import os
import json
from mako.template import Template

# config
jsonfile = open('syn.json').readlines()
jsonstr = ''
for line in jsonfile:
    jsonstr += line.rstrip()
print(jsonstr)

cfg = json.loads(jsonstr)
print(cfg)


#prj_root = '/home/xxx/prj/e100'
prj_root = cfg["prj_root"]

lib_path = cfg["lib_path"]
lib_max = cfg["lib_max"]

rtl_path = cfg["rtl_path"]
rtl_flist = cfg["rtl_flist"]

rtls = open(rtl_flist, 'r').readlines()
print(rtls)

# define template
t = """
set lib_path ${lib_path}
set ss_lib ${lib_max}
set search_path [concat $search_path $lib_path]
set target_library [list $ss_lib]
set synthetic_library [list dw_foundation.sldb]
set link_library [list * $ss_lib $synthetic_library]
% for rtl in rtls:
analyze -format verilog ${rtl}
% endfor
elaborate top
link
check_design
"""

# write syn script
print('Generate syn.tcl ...')
mytemplate = Template(t)
scr = mytemplate.render(lib_path=lib_path,
                  lib_max=lib_max,
                  rtls=rtls)
tcl = open('syn.tcl', 'w')
tcl.write(scr)
print('Done')

# Do synthesis
print('Run Command: dc_shell -f syn.tcl')
#os.system('dc_shell -f syn.tcl')
# ...

