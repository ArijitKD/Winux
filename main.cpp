#include <cstdlib>
#include<ctime>
#include<iostream>
#include<windows.h>

// no song and message = 0
// song only = 1
// message only = 2
// both song and message = 3

VOID startup(LPSTR cmdline)
{
   // additional information
   STARTUPINFO si;     
   PROCESS_INFORMATION pi;

   // set the size of the structures
   ZeroMemory( &si, sizeof(si) );
   si.cb = sizeof(si);
   ZeroMemory( &pi, sizeof(pi) );

  // start the program up
  CreateProcess(NULL,   // the path
    cmdline,           // Command line
    NULL,           // Process handle not inheritable
    NULL,           // Thread handle not inheritable
    FALSE,          // Set handle inheritance to FALSE
    0,              // No creation flags
    NULL,           // Use parent's environment block
    NULL,           // Use parent's starting directory 
    &si,            // Pointer to STARTUPINFO structure
    &pi             // Pointer to PROCESS_INFORMATION structure (removed extra parentheses)
    );
    // Close process and thread handles. 
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
}

int main(void)
{
	srand(time(0));
	int random_n = (rand() % 50) + 20;
	
	for (int i=0; i<random_n; i++)
	{
		if (i==0)
			startup((LPSTR)"winuxcore.exe 1");
		else if (i==random_n-1)
			startup((LPSTR)"winuxcore.exe 2");
		else
			startup((LPSTR)"winuxcore.exe 0");
	}
	return 0;
}