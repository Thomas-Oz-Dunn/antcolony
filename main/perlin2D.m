function map = perlin2D (size)
    map = zeros([size,size]);     % Prepare output image (size: m x m)
    w = size;
    i = 0;
    while w > 3
        i = i + 1;
        d = interp2(randn([size,size]), i-1, 'spline');
        map = map + i * d(1:size, 1:size);
        w = w - ceil(w/2 - 1);
    end
    map = (map - min(min(map(:,:)))) ./ (max(max(map(:,:))) - min(min(map(:,:))));
end