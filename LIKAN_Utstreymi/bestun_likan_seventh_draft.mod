param S >= 0 integer;
param T >= 0 integer;
param D >= 0 integer;
param A {s in 1..S};
param windowsize >= 0 integer;

/* ------ Vendorar --------*/
param O{t in 1..T} binary;
param EIM{t in 1..T} binary;
param SAM{t in 1..T} binary;
/*------------------------*/

/* ------ Breytur --------*/
var x{s in 1..S, t in 1..T, d in 1..D} binary;
var SuperAlag{t in 1..T, d in 1..D} >= 0;
var TheMaxAlag >= 0;
var MaxDagsAlag >= 0;

var LB1{t in 1..T, d in 1..D} binary;
var LB2{t in 1..T, d in 1..D} binary;
var LB3{t in 1..T, d in 1..D} binary;
var LB4{t in 1..T, d in 1..D} binary;
var LB5{t in 1..T, d in 1..D} binary;
var LB6{t in 1..T, d in 1..D} binary;
var LB7{t in 1..T, d in 1..D} binary;
/*------------------------*/


param Ttarget {t in 1..T, d in 1..D};
set Bannlisti within {s in 1..S, t in 1..T, d in 1..D};
set Fixlisti within {s in 1..S, t in 1..T, d in 1..D};


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


/* ------ Markfall & Skorður --------*/
minimize MaxAlag: 5*TheMaxAlag + sum{t in 1..T, d in 1..D} SuperAlag[t,d];

s.t. Alagsmaeling{t in 1..(T-windowsize), d in 1..D}: sum{s in 1..S, k in t..(t+windowsize)} A[s]*x[s,k,d] <= (Ttarget[t,d] + SuperAlag[t,d]);

s.t. MaxAlagMaeling{t in 1..T, d in 1..D}: TheMaxAlag >= SuperAlag[t,d];
s.t. MaxDagsAlagMaeling{d in 1..D}: sum{s in 1..S, t in 1..T} A[s]*x[s,t,d] <= MaxDagsAlag;


s.t. Bannad{(s,t,d) in Bannlisti}: x[s,t,d] = 0;
s.t. Fixed{(s,t,d) in Fixlisti}: x[s,t,d] = 1;


s.t. UseAll{s in 1..S}: sum{t in 1..T, d in 1..D} x[s,t,d] = 1;
/*---------------------------------*/



/* ------ Vendorar --------*/
s.t. SetAllO{s in Olgerdin, t in 1..T,d in 1..D}: x[s,t,d] <= O[t];
s.t. SetAllEIM{s in Eimskip, t in 1..T,d in 1..D}: x[s,t,d] <= EIM[t];
s.t. SetAllSAM{s in Samskip, t in 1..T,d in 1..D}: x[s,t,d] <= SAM[t];
/*------------------------*/

/* ------ GroupSendingar --------*/
s.t. MaxOnePerDay1{d in 1..D}: sum{t in 1..T} LB1[t,d] <= 1;
s.t. MaxOnePerDay2{d in 1..D}: sum{t in 1..T} LB2[t,d] <= 1;
s.t. MaxOnePerDay3{d in 1..D}: sum{t in 1..T} LB3[t,d] <= 1;
s.t. MaxOnePerDay4{d in 1..D}: sum{t in 1..T} LB4[t,d] <= 1;
s.t. MaxOnePerDay5{d in 1..D}: sum{t in 1..T} LB5[t,d] <= 1;
s.t. MaxOnePerDay6{d in 1..D}: sum{t in 1..T} LB6[t,d] <= 1;
s.t. MaxOnePerDay7{d in 1..D}: sum{t in 1..T} LB7[t,d] <= 1;

s.t. MaxNrOfTimeSlots1: sum{t in 1..T, d in 1..D} LB1[t,d] <= 5;
s.t. MaxNrOfTimeSlots2: sum{t in 1..T, d in 1..D} LB2[t,d] <= 5;
s.t. MaxNrOfTimeSlots3: sum{t in 1..T, d in 1..D} LB3[t,d] <= 5;
s.t. MaxNrOfTimeSlots4: sum{t in 1..T, d in 1..D} LB4[t,d] <= 5;
s.t. MaxNrOfTimeSlots5: sum{t in 1..T, d in 1..D} LB5[t,d] <= 5;
s.t. MaxNrOfTimeSlots6: sum{t in 1..T, d in 1..D} LB6[t,d] <= 5;
s.t. MaxNrOfTimeSlots7: sum{t in 1..T, d in 1..D} LB7[t,d] <= 5;

s.t. GroupSendingar1{s in Cola, t in 1..T, d in 1..D}: x[s,t,d] <= LB1[t,d];
s.t. GroupSendingar2{s in Globus, t in 1..T, d in 1..D}: x[s,t,d] <= LB2[t,d];
s.t. GroupSendingar3{s in Vintrio, t in 1..T, d in 1..D}: x[s,t,d] <= LB3[t,d];
s.t. GroupSendingar4{s in Brugghusstedja, t in 1..T, d in 1..D}: x[s,t,d] <= LB4[t,d];
s.t. GroupSendingar5{s in Dista, t in 1..T, d in 1..D}: x[s,t,d] <= LB5[t,d];
s.t. GroupSendingar6{s in Bakkus, t in 1..T, d in 1..D}: x[s,t,d] <= LB6[t,d];
s.t. GroupSendingar7{s in Mekka, t in 1..T, d in 1..D}: x[s,t,d] <= LB7[t,d];

/*--------------------------------*/


end;