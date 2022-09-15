Title: MarkovBrush

Setup:
    In main.py, the user may adjust any of the five variables starting in line 131, per the respective constraints. 
    The user may also adjust the transition matrices starting in line 105, where the commented out matrix is an example 
    of a variation. Then run the main function to run the code. A plot window with the result will eventually show,
    and the result will be saved in the directory as MarkovBrush.png.

Description of code: 
    The Python code in main.py simulates a "paintbrush" that relies on a Markov chain to move, based on a random
    walk. One transition matrix determines the direction (north, east, south, west, pause, jump) based on the current
    direction, and the other transition matrix determines the color (blue, green, red, cyan, magenta, yellow) based
    off of the current color. 

Personal Meaning:
    When I first thought of visual art and Markov chains, I considered how a painter's moving brush loosely follows some 
    sort of Markov decision process. If the brush is headed in a certain direction on a stroke, it is 

Challenge: 
This project challenged me as a computer scientist because 
because I did not have much matplotlib experience
 I pushed myself outside of my comfort zone by
had a bug where i didnt update the new color, new dirextion, new pressure etc. 
i tried to challenge myself by implementing pressure, then realized my implementation went down the wrong rabbit hole 
because they all tended to 0 ugh 

COULD CHANGE BRUSH TYPE TOO????

started to adjust matrices for color and it actually became cooler looking 

Creativity:
    Granted, I would not rush to the MoMA or the Louvre with the artifacts from my program. However, 
I do believe this system is creative because its artifacts are generated in a novel way 
   novel - it is a novel process: trying to create a JASJDJSJFJD
   valuable - trying to mimic a painter's brush reveals to us how difficult it is to predict or replicate the essence
   of human drawing or stroke making. there is not an easy recipe for directing ones hand or deciding when to switch
   colors. etc. 

definitely combinatorial - combining random walks and art and multiple markov chains

Sources:
    I based my random walk code on "Random Walk (Implementation in Python)." When I was theorizing my random walk 
    method before finding this source, I was thinking of using a matrix to track the trace of position. I really 
    liked how this source uses two simple arrays to keep track of x and y coordinates, with discrete time being the
    index of each array. 
    ( www.geeksforgeeks.org/random-walk-implementation-python/ ) 
    I did not seek any advice from colleagues on this project. 