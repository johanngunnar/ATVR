

f = open("runModelAndVisual.command","w+")

for i in range(1,52):
	f.write("glpsol --math -m bestun_likan_seventh_draft.mod -d demo_data_real{}.txt --check --wlp lp_output{}.lp\n".format(i,i))
	f.write("gurobi_cl TimeLimit=10 ResultFile=solution{}.sol lp_output{}.lp\n".format(i,i))
	f.write("\n")
f.write("python3 Visual_REALDATA_v4.py")