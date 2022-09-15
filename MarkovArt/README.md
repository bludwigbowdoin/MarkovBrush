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
    off of the current color. When the direction is jump, a compound direction process occurs, where the jump direction 
    modifies the jump size and yields to the next direction (guaranteed non-jump) for direction. 

Personal Meaning:
    As soon as we were handed this assignment, my mind went from art to paint brush to autonomous paint brush to 
    random walk to autonomous paint brush powered by Markov chains. I am not a very good painter myself, but I thought
    it would be cool (challenging at the very least) to model a moving paintbrush. The wish to see this goal through to 
    the best of my ability was what made this project personally meaningful to me at first. What gave this project 
    greater meaning to me was when I finally made my first multicolored, properly dimensioned artifact. It was indeed 
    simple, but it was also unique and fun to me. It immediately reminded me of a pixelated self-portrait of George 
    Stibitz I frequently saw in the Math/CS department of Denison University as I grew up (my dad is a math professor 
    there). George Stibitz's contribution to computing, and the similarity of my program's results to Stibitz's own 
    creations made this connection special to me. Unlike his images, mine do not have a prescribed subject, but I find 
    it fun to guess what my images could represent, as in cloud-gazing. The connection to Stibitz's self-portrait also 
    inspired me to maintain the pixel marker texture as opposed to others, though the user may make their own decision.

Challenge: 
    One of the biggest challenges I assigned myself on this project was attempting to mimic the "pressure" of the 
    brush stroke. I.e., I wanted to have the individual coordinate markers increase/decrease/maintain size based on a 
    Markov transition matrix. I had started a matrix with two degrees of multiplicative decrease (0.9, 0.8), a single 
    identity (1.0) scalar, and two degrees of multiplicative increase (1.1, 1.2). The mathematical issue I ran into 
    with this was that after many, many steps, the pressure of the stroke tended very, very small to zero. I attempted 
    to remedy this with a lower limit of 1, but then they all just tended to 1. For any non-boring pressure 
    matrix, this issue arose. Then I decided to not have a transition matrix of pressure modifiers but 5 optional 
    pressures themselves. After plenty of debugging, matplotlib still did not like my correctly-sized, correctly-float 
    array of pressures. After many hours on this pressure idea, I decided to give it up. This in itself was a challenge 
    because of the sunk costs, but I decided I could experiment with varying textures (marker shape) instead. After 
    selecting five texture options (still seen as the constants in the program), I was shortly able to implement a 
    Markov transition matrix with them. Despite it working properly, the artifacts produced were horrendous when it came
    to aesthetic appeal. So I decided to ditch that idea, too. Instead, I left it to the user to select one texture for 
    each artifact. The final challenge was manually adjusting the matrices to get aesthetically appealing artifacts. 
    The color scheme was fresh and interesting to me, so I focused on the directions. It was tough to manually translate
    desired qualities into the matrix entries, and it was frustrating to know that there were infinitely many 
    possibilities. With more time, I would have liked to explore different ways to modify the matrices outside the 
    manual option. This could be some generic input that translates "spirals" or "long lines" into matrices, or a 
    method of training the matrices on known paintings. These challenges were important for me because they made me 
    temper my perfectionism with pragmatism and reality. Even though it was hard to give up on an aspect that I had 
    invested so much time in, it was still the best move for me in the overall goal of the project. Going forward, I   
    hope to better plan out the various aspects of my projects and how much they mean to me. That way, when I am 
    particularly stumped on one part, I know whether it is absolutely crucial to keep plugging away, or whether it is 
    okay to put it on the back burner, or turn it off completely.

Creativity:
    Granted, I would not rush to the MoMA or the Louvre with the artifacts from my program. However, I do believe this 
    system is creative because its artifacts/methods are novel and valuable. The novelty comes from the fact that 
    although countless random walks exist, this program applies a new dimension that is variational color. I believe
    the process is novel as well. I have seen random walks model animate entities, but I have not seen them in the 
    context of a paint brush. I did not model a paintbrush anywhere close to realism, but the intention was there all
    the same. The value in the program comes in two forms: aesthetic appeal and revealed complexity. I personally find
    the outputs to be visually striking and appealing, though minimalistic (others may say "simple"). More 
    significantly, the process of creating this mimicry-based program reveals how complex and nuanced the motion of a 
    painter's brush is. I found it entirely difficult to predict or replicate the essence of human drawing or stroke 
    making. There is not an easy recipe to be described in a 2 dimensional matrix for directing ones hand or deciding 
    when to switch paint colors or textures. Lastly, I would say my program definitely fits under the combinatorial 
    creativity category. I aimed to combine two known entities: random walks (with Markov chains) and strokes of paint. 

Sources:
    I based my random walk code on "Random Walk (Implementation in Python)." When I was theorizing my random walk 
    method before finding this source, I was thinking of using a matrix to track the trace of position. I really 
    liked how this source uses two simple arrays to keep track of x and y coordinates, with discrete time being the
    index of each array. 
    ( www.geeksforgeeks.org/random-walk-implementation-python/ ) 
    I did not seek any advice from colleagues on this project. 