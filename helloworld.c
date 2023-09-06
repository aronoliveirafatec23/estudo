#include <stdio.h> 
  
int main() 
{ 
  
    // Declare the variables
    char str[20]; 
  
    // --- Integer --- 
  
    // Input the integer 
    printf("Enter with your name: "); 
    gets(str); 
    printf("Hello World - %s", str);
    return 0;
}