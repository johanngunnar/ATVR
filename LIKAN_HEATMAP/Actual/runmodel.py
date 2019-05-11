

f = open("runModelAndVisual.command","w+")

f.write("glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real.txt --check --wlp lp_output.lp\n")
f.write("gurobi_cl ResultFile=solution.sol lp_output.lp\n")
f.write("\n")
f.write("python3 Visual_REALDATA_v3.1.py")