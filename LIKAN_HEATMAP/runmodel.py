

f = open("runModelAndVisual.command","w+")

f.write("glpsol --math -m bestun_likan_seventh_draft.mod -d demo_data_real.txt --check --wlp lp_output.lp\n")
f.write("gurobi_cl TimeLimit=120 ResultFile=solution.sol lp_output.lp")
f.write("\n")
f.write("python3 Visual_REALDATA_v4.py")