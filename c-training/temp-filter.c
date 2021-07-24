    for (int i = 0; i < width; i = i + (width -1))
    {
        for (int j = 0; j < height; j = j + (height - 1))
        {

            //top left corner
            if (i == 0 && j == 0)
            {
                counter = 0;
                red = 0;
                green = 0;
                blue = 0;

                for (int k = 0; k < 2; k++)
                {
                    for (int l = 0; l < 2; l++)
                    {
                        red = red + image[i + k][j + l].rgbtRed;
                        green = green + image[i + k][j + l].rgbtGreen;
                        blue = blue + image[i + k][j + l].rgbtBlue;
                        counter++;
                    }
                }

                temp[i][j].rgbtRed = round (red/ counter);
                temp[i][j].rgbtBlue = round (blue/ counter);
                temp[i][j].rgbtGreen = round (green/ counter);
            }


            //right top corner
            // else if (i == 0 && j == height - 1)
            // {
            //     counter = 0;
            //     red = 0;
            //     green = 0;
            //     blue = 0;

            //     for (int k = 0; k < 2; k++)
            //     {
            //         for (int l = -1; l < 1; l--)
            //         {
            //             red = red + image[i + k][j + l].rgbtRed;
            //             green = green + image[i + k][j + l].rgbtGreen;
            //             blue = blue + image[i + k][j + l].rgbtBlue;
            //             counter++;
            //         }
            //     }


            //     temp[i][j].rgbtRed = round (red/ counter);
            //     temp[i][j].rgbtBlue = round (blue/ counter);
            //     temp[i][j].rgbtGreen = round (green/ counter);
            // }
        }
    }

    //         //left bottom corner
    //         if (i == 0 && j == height - 1)
    //         {
    //             counter = 0;
    //             red = 0;
    //             green = 0;
    //             blue = 0;

    //             for (int k = -1; k < 1; k++)
    //             {
    //                 for (int l = 0; l < 2; l++)
    //                 {
    //                     red = red + image[i + k][j + l].rgbtRed;
    //                     green = green + image[i + k][j + l].rgbtGreen;
    //                     blue = blue + image[i + k][j + l].rgbtBlue;
    //                     counter++;
    //                 }
    //             }

    //             temp[i][j].rgbtRed = round (red/ counter);
    //             temp[i][j].rgbtBlue = round (blue/ counter);
    //             temp[i][j].rgbtGreen = round (green/ counter);
    //         }


    //         //right bottom corner
    //         if (i == width - 1 && j == height - 1)
    //         {
    //             counter = 0;
    //             red = 0;
    //             green = 0;
    //             blue = 0;

    //             for (int k = -1; k < 1; k++)
    //             {
    //                 for (int l = -1; l < 1; l--)
    //                 {
    //                     red = red + image[i + k][j + l].rgbtRed;
    //                     green = green + image[i + k][j + l].rgbtGreen;
    //                     blue = blue + image[i + k][j + l].rgbtBlue;
    //                     counter++;
    //                 }
    //             }

    //             temp[i][j].rgbtRed = round (red/ counter);
    //             temp[i][j].rgbtBlue = round (blue/ counter);
    //             temp[i][j].rgbtGreen = round (green/ counter);
    //         }

    //     }
    // }