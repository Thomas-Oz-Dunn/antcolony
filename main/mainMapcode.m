clear;
clc;

i = 1;
%Generate the world
size = 100;
land = fractalMap(size,3,10,1.2,0.3,0.4);
veg = vegMap(land);
life = gameOfLife(veg);


while i < 12

    figure(i)
    imshow(life)
    
    newlife = zeros(size,size);
    newlife = gameOfLife(life);
    
    figure(i+1)
    imshow(newlife)
    
    life = zeros(size,size);
    life = newlife;
    
    i = i + 2;
end