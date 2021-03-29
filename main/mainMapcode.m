clear;
clc;

%Generate the world
WorldMap = zeros(100,100);
a = Ant;
a.xlocation = 1;
a.ylocation = 5;

if WorldMap(a.xlocation,a.ylocation) == 1
    a.hasfound = true;
end

