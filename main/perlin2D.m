function map = perlin2D (map_size,detail)
    map = zeros([map_size,map_size]);     % Prepare output image (size: m x m)
    w = map_size;
    i = 0;
    while w > detail
        i = i + 1;
        d = interp2(randn([map_size,map_size]), i-1, 'spline');
        map = map + i * d(1:map_size, 1:map_size);
        w = w - ceil(w/2 - 1);
    end
    map = (map - min(min(map(:,:)))) ./ (max(max(map(:,:))) - min(min(map(:,:))));
end