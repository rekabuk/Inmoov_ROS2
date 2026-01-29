#include <stdio.h>
#include <fcntl.h>   // File control definitions
#include <termios.h> // POSIX terminal control definitions
#include <unistd.h>  // UNIX standard function definitions
#include <errno.h>   // Error number definitions

int main() {
    int bytes_sent;

        // /dev/ttyACM0_A   Head
        // /dev/ttyACM1_A   Sys2 Left
        // /dev/ttyACM2_A   Sys1 Right

    int fd = open("/dev/ttyACM2_A", O_RDWR | O_NOCTTY | O_NDELAY);
    if (fd == -1) {
        perror("open_port: Unable to open /dev/ttyACMx_A");
        return 1;
    }

    // Configure port settings
    struct termios options;
    tcgetattr(fd, &options);
    cfsetispeed(&options, B57600); // Set baud rate
    cfsetospeed(&options, B57600);
    options.c_cflag |= (CLOCAL | CREAD); // Enable receiver and set local mode
    options.c_cflag &= ~CSIZE; 
    options.c_cflag |= CS8;    // 8 data bits
    options.c_cflag &= ~PARENB; // No parity
    options.c_cflag &= ~CSTOPB; // 1 stop bit
    tcsetattr(fd, TCSANOW, &options);

    // Prepare and send 8-byte array
    unsigned char data[4][12] = {
                                    {0x49, 0x6d, 0x40, 0x63, 0x12, 0x09, 0x74, 0x00, 0x40, 0x7e, 0x7e, 0xf9},     // 64
                                    {0x49, 0x6d, 0x40, 0x63, 0x12, 0x09, 0x74, 0x00, 0x22, 0x7e, 0x7e, 0x13},     // 34
                                    {0x49, 0x6d, 0x40, 0x63, 0x12, 0x09, 0x74, 0x00, 0x5a, 0x7e, 0x7e, 0xd9},      // 90
                                    {0x49, 0x6d, 0x40, 0x63, 0x12, 0x08, 0x74, 0x00, 0x20, 0x7e, 0x7e, 0x6b}      // shoulder 32
                                };  

    int int_select = 3;
    while (1) {
        bytes_sent = write(fd, data[int_select], 12); // Send exactly 12 bytes
 
        if (bytes_sent < 0) {
            printf("Error writing to serial port\n");
        } else {
            printf("Sent %d bytes successfully\n", bytes_sent);
        }

        sleep(1);

        //int_select = (++int_select>=3)?0:int_select;
    }
    close(fd);
    return 0;
}
