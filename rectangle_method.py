import numpy as np 

def disk_area(r_squared):  
    # We are given r^2 in the formuala for the disk so let the user pass it in 
    return r_squared * np.pi 

def kidney_equation(x):  
    # Equation of Kidney after translating to Polar, x is the angle plugged in!
    return np.cos(x) ** 3 + np.sin(x) ** 3 

def rectangle_method_polar(kidney_eq, intervals, dug_area):      
    """ 
    Function For Midpoint Method on Polar Equation with cut out area! 

    Input: 
    - kidney_eq: equation for the provided kidney  
                 (Could be generalized to function of curve) 
    - intervals: Whole number of intervals to be used in calculating 
    - dug_area: Area of disk that's been cut out of the kidney 

    Output: 
    - result: The approximation of the area under the curve after subtracting out  
              the dug area using rectangle method
    """ 
    interval_vals = np.linspace(0, 2*np.pi, intervals+1) 
    step = (2*np.pi)/intervals  
    area = 0
    for i in range(len(interval_vals)-1):     
        midpoint = (interval_vals[i] + interval_vals[i+1])/2
        area += 0.5 * step * (kidney_eq(midpoint) ** 2)   
    return area-dug_area

dug_area = disk_area(0.125) 

ans = rectangle_method_polar(kidney_equation, 10000, dug_area) 
print(f"Approximated Area: {ans}") 