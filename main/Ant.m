classdef Ant
    properties
        xlocation {x}
        ylocation {y}
        hasFound {boolean}
    end
    methods
        
        %Leave a pheremone every location been
        function [markx,marky,mapVal] = leavePheremone(curx,cury,hasFound)
            markx = curx;
            marky = cury;
            
            %if hasfound = true
            if hasFound == true
                %2 = yes direction
                mapVal = 2;
            else 
                %1 = indifferent
                mapVal = 3;
            end
        end
        
        %Write out ideas in pseudocode
        %Look at three spaces ahead of it
        %If hasFound = false & food = true, move there first priority,
            %leave posTrail
        %If hasFound = false & posTrail = true, move there second priority
            %leave posTrail
        %If hasFound = true & negTrail = true, move there third priority
            %leave posTrail
        
        
        %Move randomly until food pheremone found
        function [newx,newy] = moveAnt(curx,cury,mapVal)
            if mapVal == 1
                newx = curx + 1;
                newy = cury + 1;
            elseif mapVal == 2
                newx = curx - 1;
                newy = cury + 1;
            else
                newx = curx - 1;
                newy = cury;
            end
        end
    end
end