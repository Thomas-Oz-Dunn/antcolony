clear;
clc;

%Generate the world
WorldMap = fractalMap(100,3,40,1.2,0.3,0.4);

 map = image(WorldMap,'CDataMapping','scaled');
 disp(map)
 colorbar