#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int gray_color;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtRed == image[i][j].rgbtBlue && image[i][j].rgbtRed == image[i][j].rgbtGreen)
            {
                gray_color = image[i][j].rgbtRed;
            }
            else
            {
                gray_color = round((image[i][j].rgbtRed +  image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            }
            image[i][j].rgbtRed = gray_color;
            image[i][j].rgbtBlue = gray_color;
            image[i][j].rgbtGreen = gray_color;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed, sepiaBlue, sepiaGreen;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //calculating and rounding of to the nearest integer
            sepiaRed = floor(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue + 0.5);
            sepiaGreen = floor(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue + 0.5);
            sepiaBlue = floor(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue + 0.5);


            //assigning the sepia red value
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
            }

            //assigning the sepia blue value
            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaBlue;
            }

            //assigning the sepia green value
            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }

        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int tempRed, tempBlue, tempGreen;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            //swapping red values
            tempRed = image[i][width - j - 1].rgbtRed;
            image[i][width - j - 1].rgbtRed = image[i][j].rgbtRed;
            image[i][j].rgbtRed = tempRed;

            //swapping blue values
            tempBlue = image[i][width - j - 1].rgbtBlue;
            image[i][width - j - 1].rgbtBlue = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = tempBlue;

            //swapping green values
            tempGreen = image[i][width - j - 1].rgbtGreen;
            image[i][width - j - 1].rgbtGreen = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = tempGreen;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    int counter = 0;
    float red = 0;
    float green = 0;
    float blue = 0;


    //calculate corners

    // bottom left corner
    int a  = 0;
    int b = 0;

    for (int k = 0; k < 2; k++)
    {
        for (int l = 0; l < 2; l++)
        {
            red =  red + image[a + k][b + l].rgbtRed;
            green = green + image[a + k][b + l].rgbtGreen;
            blue = blue + image[a + k][b + l].rgbtBlue;
            counter++;
        }
    }

    temp[a][b].rgbtRed = round(red / counter);
    temp[a][b].rgbtGreen = round(green / counter);
    temp[a][b].rgbtBlue = round(blue / counter);

    // bottom right corner
    b = width - 1;
    red = 0;
    green = 0;
    blue = 0;
    counter = 0;

    for (int k = 0; k < 2; k++)
    {
        for (int l = -1; l < 1; l++)
        {
            red =  red + image[a + k][b + l].rgbtRed;
            green = green + image[a + k][b + l].rgbtGreen;
            blue = blue + image[a + k][b + l].rgbtBlue;
            counter++;
        }
    }

    temp[a][b].rgbtRed = round(red / counter);
    temp[a][b].rgbtGreen = round(green / counter);
    temp[a][b].rgbtBlue = round(blue / counter);


    // top right corner
    a = height - 1;
    red = 0;
    green = 0;
    blue = 0;
    counter = 0;

    for (int k = -1; k < 1; k++)
    {
        for (int l = -1; l < 1; l++)
        {
            red =  red + image[a + k][b + l].rgbtRed;
            green = green + image[a + k][b + l].rgbtGreen;
            blue = blue + image[a + k][b + l].rgbtBlue;
            counter++;
        }
    }

    temp[a][b].rgbtRed = round(red / counter);
    temp[a][b].rgbtGreen = round(green / counter);
    temp[a][b].rgbtBlue = round(blue / counter);


    // top left corner
    b = 0;
    red = 0;
    green = 0;
    blue = 0;
    counter = 0;

    for (int k = -1; k < 1; k++)
    {
        for (int l = 0; l < 2; l++)
        {
            red =  red + image[a + k][b + l].rgbtRed;
            green = green + image[a + k][b + l].rgbtGreen;
            blue = blue + image[a + k][b + l].rgbtBlue;
            counter++;
        }
    }

    temp[a][b].rgbtRed = round(red / counter);
    temp[a][b].rgbtGreen = round(green / counter);
    temp[a][b].rgbtBlue = round(blue / counter);



    // calculating top row and bottom row
    for (int j = 0; j <= height; j = (j + height - 1))
    {
        for (int i = 1; i < width - 1; i++)
        {
            counter = 0;
            red = 0;
            green = 0;
            blue = 0;

            // j = 0 row or first row
            if (j == 0)
            {
                for (int k = -1; k < 2; k++)
                {
                    for (int l = 0; l < 2; l++)
                    {
                        red = red + image[i + k][j + l].rgbtRed;
                        green = green + image[i +  k][j + l].rgbtGreen;
                        blue = blue + image[i +  k][j + l].rgbtBlue;
                        counter++;
                    }
                }
            }

            // j = height - 1 row or last row
            else if (j == (height - 1))
            {
                for (int k = -1; k < 2; k++)
                {
                    for (int l = -1; l < 1; l++)
                    {
                        red = red + image[i + k][j + l].rgbtRed;
                        green = green + image[i +  k][j + l].rgbtGreen;
                        blue = blue + image[i +  k][j + l].rgbtBlue;
                        counter++;
                    }
                }
            }

            //copying to the temp image
            temp[i][j].rgbtRed = round(red / counter);
            temp[i][j].rgbtGreen = round(green / counter);
            temp[i][j].rgbtBlue = round(blue / counter);

        }
    }

    //calculate left border and right border
    for (int i = 0; i <= width; i = (i + width - 1))
    {
        for (int j = 1; j < height - 1; j++)
        {
            counter = 0;
            red = 0;
            green = 0;
            blue = 0;

            //left border
            if (i == 0)
            {
                for (int k = 0; k < 2; k++)
                {
                    for (int l = -1; l < 2; l++)
                    {
                        red = red + image[i + k][j + l].rgbtRed;
                        green = green + image[i +  k][j + l].rgbtGreen;
                        blue = blue + image[i +  k][j + l].rgbtBlue;
                        counter++;
                    }
                }
            }


            //right border
            else if (i == width - 1)
            {
                for (int k = -1; k < 1; k++)
                {
                    for (int l = -1; l < 2; l++)
                    {
                        red = red + image[i + k][j + l].rgbtRed;
                        green = green + image[i +  k][j + l].rgbtGreen;
                        blue = blue + image[i +  k][j + l].rgbtBlue;
                        counter++;
                    }
                }
            }

            //copying to the temp image
            temp[i][j].rgbtRed = round(red / counter);
            temp[i][j].rgbtGreen = round(green / counter);
            temp[i][j].rgbtBlue = round(blue / counter);

        }
    }


    //calculate central matrix
    for (int i = 1; i < width - 1; i++)
    {
        for (int j = 1; j < height - 1; j++)
        {

            red = 0;
            blue = 0;
            green = 0;
            counter = 0;

            for (int k  = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    if (i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        red += image[i + k][j + l].rgbtRed;
                        blue += image[i + k][j + l].rgbtBlue;
                        green += image[i + k][j + l].rgbtGreen;
                        counter++;
                    }
                }

            }

            //copying for temp image
            temp[i][j].rgbtRed = round(red / counter);
            temp[i][j].rgbtBlue = round(blue / counter);
            temp[i][j].rgbtGreen = round(green / counter);

        }
    }


    //copy back to original image
    for (int i = 0; i < height; i++)
    {
        for (int j  = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
        }
    }

    return;
}
