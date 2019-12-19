ucsd-digital-health-data-science-L8-nlp-slides

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

