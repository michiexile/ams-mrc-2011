function pts = mvjCircle(n,eps)

if nargin < 2
    eps = 0.1;
end
if nargin < 1
    n = 20;
end

as = random('uniform',0,2*pi,1,n);
pts = [sin(as); cos(as)];
pts = pts + random('norm',0,eps,2,n);

end
