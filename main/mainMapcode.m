clear;
clc;

%Generate the world
land = fractalMap(100,3,10,1.2,0.3);
veg = vegMap(land);


map = image(land,'CDataMapping','scaled');
disp(map)
colorbar
