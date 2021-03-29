classdef Ant
    properties
        xlocation {x}
        ylocation {y}
        hasFound {boolean}
    end
    methods
        
        %Leave a pheremone every location been
        function [markx,marky,pherVal] = leavePheremone(curx,cury,hasFound)
            markx = curx;
            marky = cury;
            
            %if hasfound = true
            if hasFound == 1
                %2 = yes direction
                pherVal = 2;
            else 
                %1 = indifferent
                pherVal = 1;
            end
        end
        
        %Move randomly until food pheremone found
        function [newx,newy] = moveAnt(curx,cury,pherVal)
            if pherVal = 1
                newx = curx;
                newy = cury;
            else
        end
    end
end