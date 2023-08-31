 
# Example Python Code for User-Defined function  
def square( num ):    
    """  
    This function computes the square of the number.  
    """    
    return num**2     
object_ = square(6)    
print( "The square of the given number is: ", object_ )

# Example Python Code for calling a function  
# Defining a function    
def a_function( string ):    
    "This prints the value of length of string"    
    return len(string)    
    
# Calling the function we defined    
print( "Length of the string Functions is: ", a_function( "Functions" ) )    
print( "Length of the string Python is: ", a_function( "Python" ) )  
 