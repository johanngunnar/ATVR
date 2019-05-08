glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real1.txt --check --wlp lp_output1.lp
gurobi_cl ResultFile=solution1.sol lp_output1.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real2.txt --check --wlp lp_output2.lp
gurobi_cl ResultFile=solution2.sol lp_output2.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real3.txt --check --wlp lp_output3.lp
gurobi_cl ResultFile=solution3.sol lp_output3.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real4.txt --check --wlp lp_output4.lp
gurobi_cl ResultFile=solution4.sol lp_output4.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real5.txt --check --wlp lp_output5.lp
gurobi_cl ResultFile=solution5.sol lp_output5.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real6.txt --check --wlp lp_output6.lp
gurobi_cl ResultFile=solution6.sol lp_output6.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real7.txt --check --wlp lp_output7.lp
gurobi_cl ResultFile=solution7.sol lp_output7.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real8.txt --check --wlp lp_output8.lp
gurobi_cl ResultFile=solution8.sol lp_output8.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real9.txt --check --wlp lp_output9.lp
gurobi_cl ResultFile=solution9.sol lp_output9.lp

glpsol --math -m bestun_likan_fifth_draft_actual.mod -d demo_data_real10.txt --check --wlp lp_output10.lp
gurobi_cl ResultFile=solution10.sol lp_output10.lp

python3 Visual_REALDATA_v3.py