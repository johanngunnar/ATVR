glpsol --math -m bestun_likan_seventh_draft.mod -d demo_data_real.txt --check --wlp lp_output.lp
gurobi_cl TimeLimit=120 ResultFile=solution.sol lp_output.lp
python3 Visual_REALDATA_v4.py