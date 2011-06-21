import edu.stanford.math.plex4.*;

maxV = 50.0;
maxD = 2;

data = dlmread('grouppoints.csv');
ms = api.Plex4.createEuclideanMetricSpace(data);
ls = api.Plex4.createMaxMinSelector(ms,50);
vr = api.Plex4.createWitnessStream(ls,maxD,maxV,100);
vr.getSize()
%%
p = api.Plex4.getDefaultSimplicialAlgorithm(maxD);
i = p.computeIntervals(vr);
i = vr.transform(i);
api.Plex4.createBarcodePlot(i,'ssid',maxV);