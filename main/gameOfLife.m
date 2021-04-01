function Next = gameOfLife(Prev)

[w,h] = size(Prev);
Next = zeros(w,h);

for i = 1:w
    for j = 1:h
        
        %================================================================
        if i>1 && j > 1 && i < w && j < h %All four clear
            sumSurround = Prev(i-1,j) + Prev(i+1,j) + Prev(i,j+1) + Prev(i,j-1);
        
        elseif i == 1 %First i
            if j == 1 %First j
                sumSurround = Prev(i+1,j) + Prev(i,j+1);
                
            elseif j == h %Last j
                sumSurround = Prev(i+1,j) + Prev(i,j-1);
                
            else %Rest j
                sumSurround = Prev(i+1,j) + Prev(i,j+1) + Prev(i,j-1);
            end
            
        elseif i == w %Last i
            if j == 1 %First j
                sumSurround = Prev(i-1,j) + Prev(i,j+1);
                
            elseif j == h %Last j
                sumSurround = Prev(i-1,j) + Prev(i,j-1);
                
            else %Rest of j
                sumSurround = Prev(i-1,j) + Prev(i,j+1) + Prev(i,j-1);
            end   
            
        elseif j == 1 %Only First j, rest of i
            sumSurround = Prev(i+1,j) + Prev(i,j+1) + Prev(i-1,j);
            
        else %Only Last j, rest of i
            sumSurround = Prev(i+1,j) + Prev(i-1,j) + Prev(i,j-1);
            
        end
        %=================================================================
        
        if(Prev(i,j) == 1)
            if(sumSurround >= 2)
                Next(i,j) = 1;
            else
                Next(i,j) = 0;
            end
        end
        
        if(Prev(i,j) == 0)
            if(sumSurround == 3)
                Next(i,j) = 1;
            else
                Next(i,j) = 0;
            end
        end
    end
end