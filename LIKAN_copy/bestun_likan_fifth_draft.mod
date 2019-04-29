param S >= 0 integer;
param T >= 0 integer;
param D >= 0 integer;
param A {s in 1..S};
param windowsize >= 0 integer;


var x{s in 1..S, t in 1..T, d in 1..D} binary;

var SuperAlag{t in 1..T, d in 1..D} >= 0;
var TheMaxAlag >= 0;

var O{t in 1..T} binary;

param Ttarget {t in 1..T, d in 1..D};
set Bannlisti within {s in 1..S, t in 1..T, d in 1..D};
set Fixlisti within {s in 1..S, t in 1..T, d in 1..D};

set Olgerdin within {s in 1..S};


minimize MaxAlag: 10*TheMaxAlag + sum{t in 1..T, d in 1..D} SuperAlag[t,d];

s.t. Alagsmaeling{t in 1..(T-windowsize), d in 1..D}: sum{s in 1..S, k in t..(t+windowsize)} A[s]*x[s,k,d] <= (Ttarget[t,d] + SuperAlag[t,d]);

s.t. MaxAlagMaeling{t in 1..T, d in 1..D}: TheMaxAlag >= SuperAlag[t,d];

s.t. Bannad{(s,t,d) in Bannlisti}: x[s,t,d] = 0;
s.t. Fixed{(s,t,d) in Fixlisti}: x[s,t,d] = 1;

s.t. UseAll{s in 1..S}: sum{t in 1..T, d in 1..D} x[s,t,d] = 1;

s.t. sameO{s in Olgerdin, t in 1..T}: sum{d in 1..D} x[s,t,d] = O[t];

end;
