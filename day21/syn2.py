
import os
import json

# config
jsonfile = open('syn.json').read()
cfg = json.loads(jsonfile)
print(cfg)


#prj_root = '/home/xxx/prj/e100'
prj_root = cfg["prj_root"]

lib_path = cfg["lib_path"]
lib_max = cfg["lib_max"]

rtl_path = cfg["rtl_path"]
rtl_flist = cfg["rtl_flist"]

# write syn script
print('Generate syn.tcl ...')
tcl = open('syn.tcl', 'w')
tcl.write('set lib_path ' + lib_path + '\n')
tcl.write('set ss_lib ' + lib_max + '\n')
tcl.write('set search_path [concat $search_path $lib_path]\n')
tcl.write('set target_library [list $ss_lib]\n')
tcl.write('set synthetic_library [list dw_foundation.sldb]\n')
tcl.write('set link_library [list * $ss_lib $synthetic_library]\n')

rtls = open(rtl_flist, 'r').readlines()
for rtl in rtls:
    tcl.write('analyze -format verilog ' + rtl.rstrip() + '\n')
tcl.write('elaborate top\n')
tcl.write('link\n')
tcl.write('check_design\n')
# ... other syn script
print('Done')

# Do synthesis
print('Run Command: dc_shell -f syn.tcl')
#os.system('dc_shell -f syn.tcl')
# ...

