python3 Create_realData.py

glpsol --math -m bestun_likan_fifth_draft.mod -d demo_data_real.txt --check --wlp lp_output.lp

gurobi_cl ResultFile=solution.sol lp_output.lp

python3 Visual_REALDATA_v2.py