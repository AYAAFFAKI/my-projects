#include <stdio.h>      // For input and output functions
#include <stdlib.h>     // For system(), exit()
#include <time.h>       // For handling time
#include <unistd.h>     // For sleep() function
#include <string.h>     // For string comparison (strcmp)

// Function declarations
void displayTime();                              // Displays the current time
void countdownTimer(int N);                      // Runs a countdown for N seconds
int tranfTime(int hour, int min, int sec);       // Converts time (h, m, s) into total seconds
void setAlarm(int alarmHour, int alarmMinute);   // Waits until the alarm time and notifies the user

void main()
{
    int choice, h, m, s;     // Variables for user input
    char *qs[3];             // String to store "Y" or "N" input for repeating

choose:  // Label to return here if user wants to choose again
    system("cls");           // Clears the screen (Windows only)
    displayTime();           // Show the current time
    printf("\n");
    printf("Choices: \n1) Countdown Timer.\n2) Set Alarm.");
    printf("\nYour choice: ");
    scanf("%d", &choice);    // Get user choice

    switch (choice)
    {
        case 1: // Countdown timer
        {
            system("cls");
            displayTime();
            printf("\n");
            printf("Enter the duration (h m s): ");
            scanf("%d %d %d", &h, &m, &s);     // Get hours, minutes, seconds
            printf("\n");
            countdownTimer(tranfTime(h, m, s)); // Convert to seconds and start countdown
            sleep(2);       // Pause briefly
            goto question;  // Ask user if they want to do more
            break;
        }
        case 2: // Set alarm
        {
            system("cls");
            displayTime();
            printf("\n");
            printf("Enter the hour and minute (e.g., 13 9): ");
            scanf("%d %d", &h, &m);   // Get hour and minute for alarm
            printf("\n");
            setAlarm(h, m);          // Wait until the alarm time is reached
            sleep(2);                // Pause briefly
            goto question;
            break;
        }
        default: // If user enters an invalid option
        {
            goto choose;  // Restart the choice prompt
        }
    }

question: // Ask the user if they want to do more
    system("cls");
    displayTime();
    printf("\n");
    printf("Do you want to do something else? (Y/N) ");
    scanf("%s", qs);       // Get response
    displayTime();
    printf("\n");
    if (strcmp(qs, "Y") == 0)   // If user said yes
    {
        goto choose;
    }
    else
    {
        printf("Bye!!!");
        exit(0);  // Exit the program
    }    
}

// Function to display the current time
void displayTime()
{
    time_t T;
    time(&T);
    struct tm *local_time = localtime(&T);
    printf("\r\t\t\t\t\t\t\t%02d:%02d:%02d", 
        local_time->tm_hour, 
        local_time->tm_min, 
        local_time->tm_sec);
}

// Converts (hours, minutes, seconds) into total seconds
int tranfTime(int hour, int min, int sec)
{
    return sec + (min * 60) + (hour * 3600);
}

// Runs a countdown for N seconds
void countdownTimer(int N)
{
    for (int i = 0; i < N; i++)
    {
        displayTime();
        sleep(1);  // Wait for 1 second
    }
    printf("\n");
    displayTime();
    printf(" The end!!\n");
}

// Keeps checking the current time until it matches the alarm time
void setAlarm(int alarmHour, int alarmMinute)
{
    time_t T;
    int i = 1;
    while (i > 0)
    {
        time(&T);
        struct tm *local_time = localtime(&T);
        displayTime();
        if (alarmHour == local_time->tm_hour && 
            alarmMinute == local_time->tm_min)
        {
            printf("\t\nALARM! The time has arrived.\n");
            break;
        }
    }
}
