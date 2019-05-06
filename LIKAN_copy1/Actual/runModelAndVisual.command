python3 Create_realData.py

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real1.txt --check --wlp lp_output1.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real2.txt --check --wlp lp_output2.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real3.txt --check --wlp lp_output3.lp

gurobi_cl ResultFile=solution1.sol lp_output1.lp

gurobi_cl ResultFile=solution2.sol lp_output2.lp

gurobi_cl ResultFile=solution3.sol lp_output3.lp

python3 Visual_REALDATA_v2.py