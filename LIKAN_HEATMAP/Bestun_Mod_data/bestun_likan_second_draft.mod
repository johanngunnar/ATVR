param S >= 0 integer;
param T >= 0 integer;
param D >= 0 integer;
param A {s in 1..S};

var x{s in 1..S, t in 1..T, d in 1..D} binary;
var TheMaxAlag >= 0;

param Tmax {t in 1..T};
param Ttarget {t in 1..T};
set Bannlisti within {s in 1..S, t in 1..T};


minimize MaxAlag: TheMaxAlag;

s.t. Alagsmaeling{t in 1..T, d in 1..D}: sum{s in 1..S} A[s]*x[s,t,d] <= Ttarget[t,d] + TheMaxAlag;

s.t. Bannad{(s,t,d) in Bannlisti}:  x[s,t,d] = 0;

s.t. UseAll{s in 1..S}: sum{t in 1..T, d in 1..D} x[s,t,d] = 1;

end;

