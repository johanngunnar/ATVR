param S >= 0 integer;
param T >= 0 integer;
param D >= 0 integer;
param A {s in 1..S};
param windowsize >= 0 integer;

/* ------ Vendorar --------*/
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

/* ------ Breytur --------*/
var x{s in 1..S, t in 1..T, d in 1..D} binary;

var SuperAlag{t in 1..T, d in 1..D} >= 0;
var TheMaxAlag >= 0;

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
minimize MaxAlag: 2*TheMaxAlag + sum{t in 1..T, d in 1..D} SuperAlag[t,d];

s.t. Alagsmaeling{t in 1..(T-windowsize), d in 1..D}: sum{s in 1..S, k in t..(t+windowsize)} A[s]*x[s,k,d] <= (Ttarget[t,d] + SuperAlag[t,d]);

s.t. MaxAlagMaeling{t in 1..T, d in 1..D}: TheMaxAlag >= SuperAlag[t,d];

s.t. Bannad{(s,t,d) in Bannlisti}: x[s,t,d] = 0;
s.t. Fixed{(s,t,d) in Fixlisti}: x[s,t,d] = 1;

s.t. UseAll{s in 1..S}: sum{t in 1..T, d in 1..D} x[s,t,d] = 1;
/*---------------------------------*/


/* ------ Vendorar --------*/
s.t. SetAllO{s in Olgerdin, t in 1..T}: sum{d in 1..D} x[s,t,d] = O[t];
s.t. SetAllC{s in Cola, t in 1..T}: sum{d in 1..D} x[s,t,d] = C[t];
s.t. SetAllG{s in Globus, t in 1..T}: sum{d in 1..D} x[s,t,d] = G[t];
s.t. SetAllV{s in Vintrio, t in 1..T}: sum{d in 1..D} x[s,t,d] = V[t];
s.t. SetAllBR{s in Brugghusstedja, t in 1..T}: sum{d in 1..D} x[s,t,d] = BR[t];
s.t. SetAllDI{s in Dista, t in 1..T}: sum{d in 1..D} x[s,t,d] = DI[t];
s.t. SetAllBA{s in Bakkus, t in 1..T}: sum{d in 1..D} x[s,t,d] = BA[t];
s.t. SetAllM{s in Mekka, t in 1..T}: sum{d in 1..D} x[s,t,d] = M[t];

s.t. SetAllEIM{s in Eimskip, t in 1..T}: sum{d in 1..D} x[s,t,d] = EIM[t];
s.t. SetAllSAM{s in Samskip, t in 1..T}: sum{d in 1..D} x[s,t,d] = SAM[t];
/*------------------------*/

end;
