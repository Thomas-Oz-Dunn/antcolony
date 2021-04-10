function [new_Coord,FoundStatus,Trail] = antexplore(cur_Coord,prev_Coord,foundStatus,land,food,trails)
    %figure out the direcition facing
    
     %Look at three spaces ahead of it            
        %If hasFound = false & food = true & land = true, move there first priority,
            %leave posTrail, hasFound = true
            
        %If hasFound = false & posTrail = true & land = true, move there second priority
            %leave posTrail
            
        %If hasFound = true & homeTrail = true & land = true, move there third priority
            %leave posTrail
            
        %If hasFound = false & food = false & land = true, move there fourth priority,
            %leave homeTrail    
            
        %Else random meander
            %if hasFound = false leave homeTrail
            %if hasFound = true leave posTrail
            
end