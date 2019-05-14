TIL AÐ RUNNA ÖLLU Í EINU:

1. Runna þessari línu einu sinni til að gera hana executable: chmod u+x runModelAndVisual.command

2. Runna þessari línu til að runna bæði create data og bestun: ./runModelAndVisual.command

3. Nú er hægt að runna bæði visual: "python3 Visual_REALDATA_heatmap.py" eða "python3 Visual_REALDATA_Tafla.py"


MANUAL WAY:

glpsol --math -m model.mod -d data.dat --check --wlp lp_output.lp
gurobi_cl ResultFile=solution.sol lp_output.lp


glpsol --math -m model.mod -d demo_data_real.dat --check --wlp lp_output.lp