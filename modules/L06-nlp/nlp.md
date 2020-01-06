ucsd-digital-health-data-science-L8-nlp-slides

# 1: What is NLP

1. Psychology: human (animal) language understanding
2. Linguistics: natural language structure
3. Math: formal grammars for processing natural language
4. Engineering: computer systems that *understand* NL input and/or generate NL output
    - Understanding (NLU)
    - Generation (NLG)

::: notes

If you study the psychological processes involved when you read or write or speak natural language, then your courses and graduate studies will likely be in the Psychology or Neuroscience department.

If you study linguistics, most of your courses will be in the English department, or whatever your native language is.

If you study the engineering of NLP systems most of your classes will be in a computer science department and you will think of your job as kind of like building compilers for natural language.

If you study the grammars that are useful of NLP your classes will be in the mathematics department and you will think of your job as designing formal logic grammars and using those to generate formal logical proofs of theorems in natural language.

You will learn about all of these perspectives on NLP in this lecture.
But you will concentrate most of your effort on the engineering of NLP systems.
In my opinion, if you can build an NLP system, you will have a far deeper understanding of the psychology and
This is the most practical and aproachable aspect of NLP. You will soon learn how to build a "recipe" of computer instructions (python code) to read, understand, and generate natural language text.
Hopefully I will be able to infect you with my fascination for the magic of machines that can interact with us in our own language so well that we can hardly tell they are not human.
It's scary and inspiring at the same time.

:::

[Foundational Issues in Natural Language Processing: Introduction](https://dash.harvard.edu/bitstream/handle/1/17017334/finlp.pdf), Sells, Peter, Stuart M. Shieber, and Thomas Wasow. 1991. (c) MIT Press.

# 2: Magical Valley of NLP

![Mashiro Mori's Uncanny Valley diagram. This shows user satisfaction with humanoid robotics technology on teh vertical axis. The horizontal axis shows the advancement of technology and time. More advanced technologies are shown on the right of the plot. As technology advances from left to right there is a gradual increase in satisfaction with technology until it reaches the lip of the uncanny valley and user satisfaction drops while anxiety increases, due to the creepiness of some advanced robotic systems. to the right of this dip, customer satisfaction climbs again as technology advances and we forget that the machine is not a human.](media/uncanny_valley.png)

::: notes

Diagram alt text: ...

Let's explore deep into the uncanny valley together.

The diagram here was sketched by Mashiro Mori in 1970, just as personal computers were being developed and systems like conversational AI programs like ELIZA were becoming popular.

Systems that look like a human body, but don't act like them probably trigger an emotional response similar to what you experience when you see a dead body (corpse) or see a zombie movie.
We have probably evolved to detect the subtle behavioral cues of sickness or mental illness.
This same discomfort with humanoid robots can also sometimes be triggered by chatbots, estpecially if the bot is given a voice that sounds relatively human.
See if you can sense your own creepiness as you have a conversation with Alexa or Google Assistant.
Those engineers have worked very hard to ensure that you don't get creeped out.
This isn't the creepiness you feel when it seems like the bot anticipates your actions before you even know you are going to do something.
This is the creepiness of hearing some subtle cues in the voice that is unnatural, while at the same time imagining that it is a human mind at work.


:::

[Uncanny Valley](https://en.wikipedia.org/wiki/Uncanny_valley#/media/File:Mori_Uncanny_Valley.svg)
[Mashiro Mori](https://en.wikipedia.org/wiki/Masahiro_Mori_(roboticist))

# 4: Language Model

Your blood pressure is too ______ .

How old are ________ ?

Does it hurt when you ________ ?

Do you have a family history of ________ ?

Dr. ________ told me the diagnosis .

Patient LDL level is 100, ________ level is 50, and the total is            .

Dr. Smith gave me ________ best estimate .


# 5: Your blood pressure is too

P=0.65   high

P=0.30   low

P=0.05   erratic


::: notes

Your
:::

# 6: How old are

P=0.95   you

P=0.03   they

P=0.01   y'all

P=0.01   yous

# 7: Does it hurt

How old are you? P=0.95

How old are they? P=0.03

How old are y'all? P=0.01

How old are yous? P=0.01


Do you have a family history of ________ ?

Dr. ________ told me the diagnosis .

Patient LDL level is 100, ________ level is 50, and the total is            .

Dr. Smith gave me ________ best estimate .


# 3: Monty Hall Fallacy

Real life applications:

- you suspect a patient has one of 3 genes that could cause a disease and you plan to treat based on that one genetic abnormality, then another doctor does a test that confirms the patient does not have one of the others. Should you change your treatment? (must assume that only 1 Gene is present otherwise the abnormality would be greater and the cause obvious, like XOR condition).
- collider on the door chosen to be opened by Monty Hall

# 4: Explain Away Fallacy

- collider where one cause negates the other
- two possible causes of test results then find out that one cause is present, that makes it less likely that the other cause is present

# 5: Berkson's Paradox

- 2 diseases required for admission to hospital (admission's bias) causing `bone disease` and `resperatory disease` to be correlated

                   , general populaiton, general populaiton, general populaiton, hospitalized
resperatory disease, bone disease yes,    bone disease no,   % bone disease,


# 6: Before Cause there was Corroboration

- strength of correlation
- agreement with physics
-

