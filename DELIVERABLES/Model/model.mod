param S >= 0 integer; 			/*-Number of shipments-*/
param T >= 0 integer; 			/*-Number of timeslots-*/
param D >= 0 integer; 			/*-Number of days-*/
param A {s in 1..S};  			/*-Parameter for alag-*/
param windowsize >= 0 integer;

/* ------ FIXED VENDORS --------*/
param O{t in 1..T} binary;
param C{t in 1..T} binary;
param G{t in 1..T} binary;
param V{t in 1..T} binary;
param BR{t in 1..T} binary;
param DI{t in 1..T} binary;
param BA{t in 1..T} binary;
param M{t in 1..T} binary;
param EIM{t in 1..T} binary;
param SAM{t in 1..T} binary;
/*------------------------*/

/* ------ VARIABLES --------*/
var x{s in 1..S, t in 1..T, d in 1..D} binary;	/*-Shipments-*/
var SuperAlag{t in 1..T, d in 1..D} >= 0;

var MaxDagsAlag >= 0;

var TheMaxAlagO >= 0;
var TheMaxAlagC >= 0;
var TheMaxAlagVandG >= 0;
var TheMaxAlagBRandDI >= 0;
var TheMaxAlagBA >= 0;
var TheMaxAlagM >= 0;
var TheMaxAlagEIM >= 0;
var TheMaxAlagSAM >= 0;

var OLG{t in 1..T, d in 1..D} binary;
var LB1{t in 1..T, d in 1..D} binary;
var LB2{t in 1..T, d in 1..D} binary;
var LB3{t in 1..T, d in 1..D} binary;
var LB4{t in 1..T, d in 1..D} binary;
var LB5{t in 1..T, d in 1..D} binary;
var LB6{t in 1..T, d in 1..D} binary;
var LB7{t in 1..T, d in 1..D} binary;
var EIMSKIP{t in 1..T, d in 1..D} binary;
var SAMSKIP{t in 1..T, d in 1..D} binary;
/*------------------------*/


param Ttarget {t in 1..T, d in 1..D};
/* ------ NOT IN USE--------*/
set Bannlisti within {s in 1..S, t in 1..T, d in 1..D};
set Fixlisti within {s in 1..S, t in 1..T, d in 1..D};
/*--------------------------*/

/*------ Vendorar ------*/
set Olgerdin within {s in 1..S};
set Cola within {s in 1..S};
set Globus within {s in 1..S};
set Vintrio within {s in 1..S};
set Brugghusstedja within {s in 1..S};
set Dista within {s in 1..S};
set Bakkus within {s in 1..S};
set Mekka within {s in 1..S};
set Eimskip within {s in 1..S};
set Samskip within {s in 1..S};
/*------------------------*/
/*
					+ TheMaxAlagO 
					+ TheMaxAlagC 
					+ TheMaxAlagVandG 
					+ TheMaxAlagBRandDI
					+ TheMaxAlagBA 
					+ TheMaxAlagM 
					+ TheMaxAlagEIM
					+ TheMaxAlagSAM
*/

/* ------ Markfall & Skorður --------*/
minimize MaxAlag: 	sum{t in 1..T, d in 1..D} SuperAlag[t,d] 
					+ TheMaxAlagO 
					+ TheMaxAlagC 
					+ TheMaxAlagVandG 
					+ TheMaxAlagBRandDI
					+ TheMaxAlagBA 
					+ TheMaxAlagM 
					+ TheMaxAlagEIM
					+ TheMaxAlagSAM
					+ 30*MaxDagsAlag;		  
					/*+ sum{t in 1..T, d in 1..D}(OLG[t,d] + LB1[t,d] + LB2[t,d] + LB3[t,d] + LB4[t,d] + LB5[t,d] + LB6[t,d] + LB7[t,d] + EIMSKIP[t,d] + SAMSKIP[t,d]);*/

s.t. Alagsmaeling{t in 1..(T-windowsize), d in 1..D}: sum{s in 1..S, k in t..(t+windowsize)} A[s]*x[s,k,d] <= (Ttarget[t,d] + SuperAlag[t,d]);

s.t. MaxAlagMaelingO{t in 1..1, d in 1..D}: TheMaxAlagO >= SuperAlag[t,d];
s.t. MaxAlagMaelingC{t in 2..2, d in 1..D}: TheMaxAlagC >= SuperAlag[t,d];
s.t. MaxAlagMaelingVandG{t in 3..3, d in 1..D}: TheMaxAlagVandG >= SuperAlag[t,d];
s.t. MaxAlagMaelingBRandDI{t in 4..4, d in 1..D}: TheMaxAlagBRandDI >= SuperAlag[t,d];
s.t. MaxAlagMaelingBA{t in 5..5, d in 1..D}: TheMaxAlagBA >= SuperAlag[t,d];
s.t. MaxAlagMaelingM{t in 6..6, d in 1..D}: TheMaxAlagM >= SuperAlag[t,d];
s.t. MaxAlagMaelingEIM{t in 7..7, d in 1..D}: TheMaxAlagEIM >= SuperAlag[t,d];
s.t. MaxAlagMaelingSAM{t in 8..8, d in 1..D}: TheMaxAlagSAM >= SuperAlag[t,d];

s.t. MaxDagsAlagMaeling{d in 1..D}: sum{s in 1..S, t in 1..T} A[s]*x[s,t,d] <= MaxDagsAlag;


s.t. Bannad{(s,t,d) in Bannlisti}: x[s,t,d] = 0;
s.t. Fixed{(s,t,d) in Fixlisti}: x[s,t,d] = 1;


s.t. UseAll{s in 1..S}: sum{t in 1..T, d in 1..D} x[s,t,d] = 1;
/*---------------------------------*/


/* ------ PLACE SHIPMENTS IN APPROPRIATE SLOT --------*/
s.t. SetAllO{s in Olgerdin, t in 1..T,d in 1..D}: x[s,t,d] <= O[t];
/*
s.t. SetAllC{s in Cola, t in 1..T, d in 1..D}: x[s,t,d] <= C[t];
s.t. SetAllG{s in Globus, t in 1..T, d in 1..D}: x[s,t,d] <= G[t];
s.t. SetAllV{s in Vintrio, t in 1..T, d in 1..D}: x[s,t,d] <= V[t];
s.t. SetAllBR{s in Brugghusstedja, t in 1..T, d in 1..D}: x[s,t,d] <= BR[t];
s.t. SetAllDI{s in Dista, t in 1..T, d in 1..D}: x[s,t,d] <= DI[t];
s.t. SetAllBA{s in Bakkus, t in 1..T, d in 1..D}: x[s,t,d] <= BA[t];
s.t. SetAllM{s in Mekka, t in 1..T, d in 1..D}: x[s,t,d] <= M[t];
s.t. SetAllEIM{s in Eimskip, t in 1..T,d in 1..D}: x[s,t,d] <= EIM[t];
s.t. SetAllSAM{s in Samskip, t in 1..T,d in 1..D}: x[s,t,d] <= SAM[t];
*/
/*----------------------------------------------------*/

/* ------ GroupSendingar --------*/
s.t. MaxOnePerDayOLG{d in 1..D}: sum{t in 1..T} OLG[t,d] <= 1;
s.t. MaxOnePerDay1{d in 1..D}: sum{t in 1..T} LB1[t,d] <= 1;
s.t. MaxOnePerDay2{d in 1..D}: sum{t in 1..T} LB2[t,d] <= 1;
s.t. MaxOnePerDay3{d in 1..D}: sum{t in 1..T} LB3[t,d] <= 1;
s.t. MaxOnePerDay4{d in 1..D}: sum{t in 1..T} LB4[t,d] <= 1;
s.t. MaxOnePerDay5{d in 1..D}: sum{t in 1..T} LB5[t,d] <= 1;
s.t. MaxOnePerDay6{d in 1..D}: sum{t in 1..T} LB6[t,d] <= 1;
s.t. MaxOnePerDay7{d in 1..D}: sum{t in 1..T} LB7[t,d] <= 1;
s.t. MaxOnePerDayEIMSKIP{d in 1..D}: sum{t in 1..T} EIMSKIP[t,d] <= 1;
s.t. MaxOnePerDaySAMSKIP{d in 1..D}: sum{t in 1..T} SAMSKIP[t,d] <= 1;

s.t. GroupSendingarOLG{s in Olgerdin, t in 1..T, d in 1..D}: x[s,t,d] <= OLG[t,d];
s.t. GroupSendingar1{s in Cola, t in 1..T, d in 1..D}: x[s,t,d] <= LB1[t,d];
s.t. GroupSendingar2{s in Globus, t in 1..T, d in 1..D}: x[s,t,d] <= LB2[t,d];
s.t. GroupSendingar3{s in Vintrio, t in 1..T, d in 1..D}: x[s,t,d] <= LB3[t,d];
s.t. GroupSendingar4{s in Brugghusstedja, t in 1..T, d in 1..D}: x[s,t,d] <= LB4[t,d];
s.t. GroupSendingar5{s in Dista, t in 1..T, d in 1..D}: x[s,t,d] <= LB5[t,d];
s.t. GroupSendingar6{s in Bakkus, t in 1..T, d in 1..D}: x[s,t,d] <= LB6[t,d];
s.t. GroupSendingar7{s in Mekka, t in 1..T, d in 1..D}: x[s,t,d] <= LB7[t,d];
s.t. GroupSendingarEIMSKIP{s in Eimskip, t in 1..T,d in 1..D}: x[s,t,d] <= EIMSKIP[t,d];
s.t. GroupSendingarSAMSKIP{s in Samskip, t in 1..T,d in 1..D}: x[s,t,d] <= SAMSKIP[t,d];

s.t. MaxNrOfTimeSlotsOLG: sum{t in 1..T, d in 1..D} OLG[t,d] <= 5;
s.t. MaxNrOfTimeSlots1: sum{t in 1..T, d in 1..D} LB1[t,d] <= 5;
s.t. MaxNrOfTimeSlots2: sum{t in 1..T, d in 1..D} LB2[t,d] <= 5;
s.t. MaxNrOfTimeSlots3: sum{t in 1..T, d in 1..D} LB3[t,d] <= 5;
s.t. MaxNrOfTimeSlots4: sum{t in 1..T, d in 1..D} LB4[t,d] <= 5;
s.t. MaxNrOfTimeSlots5: sum{t in 1..T, d in 1..D} LB5[t,d] <= 5;
s.t. MaxNrOfTimeSlots6: sum{t in 1..T, d in 1..D} LB6[t,d] <= 5;
s.t. MaxNrOfTimeSlots7: sum{t in 1..T, d in 1..D} LB7[t,d] <= 5;
s.t. MaxNrOfTimeSlotsEIMSKIP: sum{t in 1..T, d in 1..D} EIMSKIP[t,d] <= 5;
s.t. MaxNrOfTimeSlotsSAMSKIP: sum{t in 1..T, d in 1..D} SAMSKIP[t,d] <= 5;
/*--------------------------------*/


end;