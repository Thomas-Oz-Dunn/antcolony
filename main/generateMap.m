function map = generateMap(size,detail)
    map = perlin2D(size,detail);
    for i = 1:size
        for j = 1:size
            if map(i,j) > 0.5
                map(i,j) = 1; %Walls
            else
                map(i,j) = 0; %Paths
            end
        end
    end
end
% map = image(mapGen,'CDataMapping','scaled'); for visuals
