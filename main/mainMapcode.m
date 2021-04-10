clear;
clc;

i = 1;

%Generate the world
size = 100;
land = fractalMap(size,3,10,1.2,0.3,0.4);
veg = vegMap(land);
