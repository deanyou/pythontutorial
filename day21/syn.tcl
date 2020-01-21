set lib_path ./syn
set ss_lib slow.db
set search_path [concat $search_path $lib_path]
set target_library [list $ss_lib]
set synthetic_library [list dw_foundation.sldb]
set link_library [list * $ss_lib $synthetic_library]
analyze -format verilog a.v
analyze -format verilog b.v
analyze -format verilog c.v
elaborate top
link
check_design
