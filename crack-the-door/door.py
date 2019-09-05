import angr
import claripy

proj = angr.Project('./Crack_The_Door')
initial_state = proj.factory.entry_state(args="./Crack_The_Door",load_options={"auto_load_libs":False})
sm = proj.factory.simulation_manager(initial_state)
sm.explore(find=0x401AB6, avoid=0x401AD4)
found = sm.found[0]
import IPython
IPython.embed()
print('done?')

