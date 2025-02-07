### INITIAL COMMENTS ###

#TITLE
#Name of file holding program
#Created by: Ruby Radosevic and Carlos Manzo
#Contact at: rubyaradosevic@lewisu.edu and {CARLO'S EMAIL}
#Course: Software Engineering 44000 - LT1
#Completed on: DATE OF SUBMISSION
#Program explanation
#Any resources used {?}

### NOTES - TO BE DELETED ###

#Each declaration should include a comment explaining its use
#Each subprogram (function,subroutine,object) should have an opening comment describing its purpose
#Each loop should be preceded by a comment that describes its purpose
#Any statement that is particularly unclear or tricky should have a clarifying comment

#near-miss(x,y,z,n,k)
#2 < n < 12
#10 <=x <= k
#10 <=y <= k

#NOTES: program takes n for the power, and k, which should be AT LEAST >=10 AND have an upper limit to stop crashing


### PROGRAM ###

#NEAR_MISS_ITERATION: solves for z value, actual miss, and relative miss for one x and y value
def near_miss_iteration(n,x,y):
    left_side = x**n + y**n
    z=0

    #Takes larger between x and y as starting point, and continues to iterate through until z^2 >= left_side
    if x >= y:
        while z**n < left_side:
            z+= 1
    
    else:
        while z**n < left_side:
            z+= 1
    
    #Determines if z or z+1 is the closer near miss
    #Near_miss_iteration returns: x,y,z, actual miss, relative miss as a LIST
    if z**n - left_side < (z+1)**n - left_side:
        return ([x,y,z, (z**n - left_side), ((z**n - left_side) / left_side)])
    
    else:
        return ([x,y,z, ((z + 1)**n - left_side), (((z + 1)**n - left_side) / left_side)])
    

#ITERATE through all possible x and y natural numbers, tracking lowest relative miss

#FOR EACH NEW SMALLEST RELATIVE MISS: PRINT current x,y,z, actual miss (x^n + y^n) - ( (z+=1) ^ n) and
#relative miss ( (x^n + y^n) - ( (z+=1) ^ n) ) / (x^n + y^n)

### SUBMISSION RULES ###

#Submit only the clone command; I will run it according to the readme file that should be available on github
#Include necessary libraries