Describe how the system is personally meaningful to you (at least 1 paragraph).
Explain how working on it genuinely challenged you as a computer scientist (at least 1 paragraph).
    How did you push yourself outside of your comfort zone?
    Why was this an important challenge for you?
    What are the next steps for you going forward?
Include a discussion of whether you believe your system is creative (and why or why not).


Title: MarkovBrush

Setup:
    In main.py, choose a start_direction, start_color, path_length, and jump_size, considering the restrictions in the 
    relevant comments. Then run the main function to run the code. A plot window with the result will eventually show,
    and the result will be saved in the directory as MarkovBrush.png

Description of code: 
    


1. When I first thought of visual art and Markov chains, I considered how a painter's moving brush loosely follows some 
sort of Markov decision process. If the brush is headed in a certain direction on a stroke, it is 

2. This project challenged me as a computer scientist because 
because I did not have much matplotlib experience
 I pushed myself outside of my comfort zone by
had a bug where i didnt update the new color, new dirextion, new pressure etc. 
i tried to challenge myself by implementing pressure, then realized my implementation went down the wrong rabbit hole 
because they all tended to 0 ugh 

COULD CHANGE BRUSH TYPE TOO????

3. I do believe this system is creative because its artifacts are generated in a novel way 
   novel - it is a novel process: trying to create a JASJDJSJFJD
   valuable - trying to mimic a painter's brush reveals to us how difficult it is to predict or replicate the essence
   of human drawing or stroke making. there is not an easy recipe for directing ones hand or deciding when to switch
   colors. etc. 

definitely combinatorial - combining random walks and art and multiple markov chains

4. Sources: 
    I based my random walk code on "Random Walk (Implementation in Python)." When I was theorizing my random walk 
    method before finding this source, I was thinking of using a matrix to track the trace of position. I really 
    liked how this source uses two simple arrays to keep track of x and y coordinates, with discrete time being the
    index of each array. 
    ( www.geeksforgeeks.org/random-walk-implementation-python/ ) 
    I did not seek any advice from colleagues on this project. 