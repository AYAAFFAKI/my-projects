#include <stdio.h>      // for input/output functions
#include <math.h>       // for math functions like sin, cos, pow, sqrt, etc.
#include <string.h>     // for string comparison (strcmp)

// Entry point of the program
int main ()
{   
    int opinion, n;           // Variables to store user option and integer input
    char c[10];               // Array to store operation strings like "+", "sin", etc.
    double a, b;              // Variables for numeric inputs

    // Display menu of operations
    printf("We have the following operations:");
    printf("\n\t1)normal operation \t\t6)factorial");
    printf("\n\t2)trigonometric \t\t7)exponential");
    printf("\n\t3)square root \t\t\t8)logarithm");
    printf("\n\t4)nth root \t\t\t9)logarithm of base a");
    printf("\n\t5)power \t\t\t10)absolute value");

    int j = 1;  // Loop control variable
    while (j > 0)
    {   
        // Ask user to choose an operation
        printf("\nchoose a number: ");
        scanf("%d", &opinion);

        // Perform corresponding operation based on user input
        switch (opinion)
        {
            case 1: // Basic arithmetic (+, -, *, /)
            {
                printf("Give two numbers: ");
                scanf("%lf %lf", &a, &b);
                printf("Give the operation:");
                scanf("%s", c);

                // Compare input to perform the correct arithmetic operation
                if (strcmp(c, "+") == 0)
                    printf("\n\tThe result is: %.2lf.", a + b);
                else if (strcmp(c, "-") == 0)
                    printf("\n\tThe result is: %.2lf.", a - b);
                else if (strcmp(c, "*") == 0)
                    printf("\n\tThe result is: %.2lf.", a * b);
                else if (strcmp(c, "/") == 0)
                {
                    if (b == 0)
                        printf("Error!!!!!!!!"); // Division by zero check
                    else
                        printf("\n\tThe result is: %.2lf", a / b);  
                }
                else
                    printf("\n\tError, Give a normal operation!!");
                break;
            }
            case 2: // Trigonometric functions (sin, cos, tan)
            {
                printf("Give the operation:");
                scanf("%s", c);

                // Convert degrees to radians before applying trig functions
                if (strcmp(c, "cos") == 0)
                {
                    printf("Give the number in degrees: ");
                    scanf("%lf", &a);
                    b = (a * M_PI) / 180;
                    printf("\n\tcos(%.2lf): %.2lf", a, cos(b));
                }
                else if (strcmp(c, "sin") == 0)
                {
                    printf("Give the number in degrees: ");
                    scanf("%lf", &a);
                    b = (a * M_PI) / 180;
                    printf("\n\tsin(%.2lf): %.2lf", a, sin(b));
                }
                else if (strcmp(c, "tan") == 0)
                {
                    printf("Give the number in degrees: ");
                    scanf("%lf", &a);
                    if (a == 90)
                        printf("Error!!!!!!!!"); // tan(90°) is undefined
                    else
                    {
                        b = (a * M_PI) / 180;
                        printf("\n\ttan(%.2lf): %.2lf", a, tan(b));
                    }
                }
                else
                    printf("\n\tError, Give a trigonometric operation!!");
                break;
            }
            case 3: // Square root
            {
                printf("Give a number:");
                scanf("%lf", &a);
                printf("\n\tThe result is: %.4lf", sqrt(a));
                break;
            }
            case 4: // Nth root
            {
                printf("Give the value of the root: ");
                scanf("%lf", &b);
                printf("Give a number: ");
                scanf("%lf", &a);
                printf("The result is: %.4lf", pow(a, (1 / b)));
                break;
            }
            case 5: // Power
            {
                printf("Give the exponent value:");
                scanf("%d", &n);
                printf("Give a number:");
                scanf("%lf", &a);
                printf("%.2lf exponent %d is: %.2lf", a, n, pow(a, n));
                break;
            }
            case 6: // Factorial
            {   
                int M, i;
                printf("Give a value of n: ");
                scanf("%d", &n);
                if (n == 1 || n == 0)
                    printf("n! = 1");
                else
                {
                    M = 1;
                    for (i = 2; i <= n; i++)
                        M = M * i;
                    printf("\n\tn! = %d", M);
                }
                break;
            }
            case 7: // Exponential function (e^x)
            {
                printf("Give a value of x: ");
                scanf("%lf", &a);
                printf("\n\texponential is: %.2lf", exp(a));
                break;
            }
            case 8: // Natural logarithm (log base e)
            {
                printf("Give a value of x: ");
                scanf("%lf", &a);
                printf("\n\tlogarithm is: %.2lf", log(a));
                break;
            }
            case 9: // Logarithm of base a
            {
                printf("Give the base a then x: ");
                scanf("%lf %lf", &a, &b);
                printf("\n\tlogarithm of base %.2lf is: %.3lf", a, (log(b) / log(a)));
                break;
            }
            case 10: // Absolute value
            {
                printf("Give a number:");
                scanf("%lf", &a);
                printf("\n\t|%.2lf| = %.2lf", a, fabs(a));
                break;
            }
            default: // Invalid operation input
            {
                printf("Invalid number:\n");
                break;
            }
        }

        // Ask the user whether to perform another calculation
        char qs[5];
        printf("\n\t\t*Do you have an additional calculation?(yes/no)");
        scanf("%s", qs);
        if (strcmp(qs, "no") == 0)
        {
            printf("\n\t***BYE!!*");
            break;
        }
        j++;  // Continue loop if user wants to calculate more
    }

    return 0; // End of program
}
