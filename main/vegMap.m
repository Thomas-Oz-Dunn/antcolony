function vegMap = vegMap(landmap)

    [w,h] = size(landmap);
    RanMap = perlin2D(w,7);
    
    vegMap = zeros([w,h]);
    for i = 1:w
       for j = 1:h
          if RanMap(i,j) > 0.1
              RanMap(i,j) = 1;
          else
              RanMap(i,j) = 0;
          end
          if(landmap(i,j) == 1 && RanMap(i,j) == 1)
              vegMap(i,j) = 1;
          end
       end
    end
end