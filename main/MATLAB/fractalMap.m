function map = fractalMap(size,min_detail,max_detail,weight1,weight2,threshold)
    
    map = sparse(size,size);
    map1 = perlin2D(size,min_detail);
    map2 = perlin2D(size,max_detail);
    for i = 1:size
        for j = 1:size
            map(i,j) = (weight1*map1(i,j) + weight2*map2(i,j))/2;
            if map(i,j) > threshold
                map(i,j) = 1; 
            end
        end
    end
end

