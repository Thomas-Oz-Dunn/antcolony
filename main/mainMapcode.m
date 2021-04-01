clear;
clc;

i = 2;
%Generate the world
land = fractalMap(100,3,10,1.2,0.3,0.4);
veg = vegMap(land);
life = gameOfLife(veg);
newlife = zeros(size(life));

while i < 12
    figure(i)
    imshow(life)
    newlife = gameOfLife(life);
    figure(i+1)
    imshow(newlife)
    life = newlife;
    i = i + 2;
end