param S >= 0 integer;
param T >= 0 integer;
param A {s in 1..S};
param Z >= 0 integer;

var x{s in 1..S, t in 1..T} binary;

param Tmax {t in 1..T};
set Bannlisti within {s in 1..S, t in 1..T};


minimize MaxAlag: Z;

s.t. Bannad{(s,t) in Bannlisti}:  x[s,t] = 0;

s.t. UseAll{s in 1..S}: sum{t in 1..T} x[s,t] = 1;

s.t. Maxid{t in 1..T}: sum{s in 1..S} A[s]*x[s,t] <= Tmax[t];

s.t. Zetan{t in 1..T}: sum{s in 1..S} A[s]*x[s,t] <= Z;

end;

