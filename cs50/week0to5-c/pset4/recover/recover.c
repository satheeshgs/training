#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //checking for 1 command line argument to be passed
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    //open file using fopen
    FILE *file = fopen(argv[1], "r");

    //check that the input file opened is not an empty file
    if (file == NULL)
    {
        printf("Empty file detected! Exiting program.\n");
        return 2;
    }


    //define variables required
    BYTE buffer[512];
    int count = 0;
    char filename[8];
    int img_found = 0;
    FILE *img_output = NULL;


    //read the bytes 512 at a time
    while (fread(buffer, 512, 1, file) == 1)
    {
        //checking for first 4 bytes for the header of a JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (img_found == 1)
            {
                fclose(img_output); //close the current file if an image header is already found
            }
            else
            {
                img_found = 1;
            }

            //start a new file with the number format ### starting with 000
            sprintf(filename, "%03i.jpg", count);
            img_output = fopen(filename, "a");
            count++;
        }
        //write to file the current byte
        if (img_found == 1)
        {
            fwrite(buffer, 512, 1, img_output);
        }
    }

    fclose(file);
    fclose(img_output);

    return 0;
}


