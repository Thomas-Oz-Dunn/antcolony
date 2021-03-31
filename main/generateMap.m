clear;
clc;
size = 64;

mapGen = perlin2D(size);
for i = 1:size
    for j = 1:size
        if mapGen(i,j) > 0.5
            mapGen(i,j) = 1;
        else
            mapGen(i,j) = 0;
        end
    end
end
x = image(mapGen,'CDataMapping','scaled');
disp(x)