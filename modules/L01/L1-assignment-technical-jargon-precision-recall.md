# Assignment: Play with Neural Nets

1. Visit playground.tensorflow.org
2. Select the spiral dataset and add 20% Noise
3. Add and remove different combinations of features: x1, x2, x1^2, x2^2, x1*x2, sin(x1), sin(x2)
4. Play around with different numbers of “HIDDEN LAYERS” and neurons per layer.
5. What is the fewest number of features, hidden layers and total neurons that you needed to achieve less than 15% loss?

# Walkthougth: Play with Neural Nets

Introduction to playground.tensorflow.org


# Technical Jargon

There are two main purposes technical jargon

- Precise communication
- Expertise signaling

<aside class='notes'>
When you go to see your doctor and you ask them a question about a technical detail about an injury, they might use words like "anterior", "posterior", "ventral", "dorsal", "distal", or "lateral" to describe the location of the injury.  If you ask them about a systemic disease they might use words like "pulmonary", "cardiac", "lymbic", "vascular", or "renal" to describe the system that is having difficulty. These are technical terms that mean something very precise to the doctor, but very little to you. So why doesn't the doctor use "layman" terms for those things, like "front" and "back" for "anterior" and "posterior", or "kidney" and "heart" for "renal" and "cardiac"? There are two reasons. It's usually habit and the doctor can switch gears back to laymans terminology if he senses your confusion. But why is the doctor trained to use these terms so consistently? The reason is likely that it is a more clear and precise way of indicating what you are talking about. Front and back don't mean exactly the same thing as anterior and posterior. And there's really not a good single laymans term to use for the "lymbic system". So that's good. There's another reason too. To signal expertise. You want to know that your doctor is a licensed medical professional that knows all the latest terminology and technology in medicine. So it's good that he signals this expertise to you through his vocabulary. It helps put you at ease and take his advice on things that he knows more about than you do, even though it's your body.

Data scientists do this too. But it may seem a bit like posturing when a statistician or computer scientist does it. That's understandable. There is no Data Science certification that reuires 12 years of training to acquire, as there is in medicine. So don't worry if you don't find yourself using terminology like "precision" and "recall" in your conversations with your colleagues. You're just being more approachable and understandable to the business folks in the room. That's a good thing. But when you want to convince people that you know what you're talking about, say in an interview or a trade show, you probably want to use the correct data science terminology.
</aside>



# T1-Q1: Applications

List at least two applications of Data Science to Healthcare.

# T1-A1: Applications

1. Clinical diagnosis
2. Radiology
3. Hospital system improvement (Population health)
4. Epidemic forecasting (Epidemiology)
5. Genomics
6. Clinical disease prediction (Kidney disease)
7. Identify possible causes of disease (Smoking -> Lung disease)



# T2-Q2: Iron Triangle

What is the Iron Triangle of healthcare?

# T2-A2: Iron Triangle

The Iron Triangle represents the belief that there are rigid constraints on the tradeoffs between healthcare cost (affordability), access (choice), and quality. It is the belief that if cost is reduced then so must the quality or the availability or treatment options. Likewise it is the belief that if healthcare quality is improved then quality or access to healthcare will suffer.



# T2-Q3: AI

Will AI replace doctors in the next 20 years? Why or why not?

# T2-A3: AI

No. Because machines and artificial intelligence software will not be able to:

1. perform all forms of surgery without supervision by an expert,

2. exercise creativity and generalization in the face of new circumstances or conditions,

3. nor exercise judgment that takes into account the payoff and risks for the patient in terms of the quality of life dimensions that are important to the patient and society

Some of the responsibilities of doctors will be significantly reduced, such as the need to make diagnosis based on radiology imagery, monitor for and predict drug interactions, side effects, and predicting the likelihood of a particular diagnosis being correct. However, doctors will then be able to use more of their time doing those things that machines will likely not do as well:

1. communicating with patients to gather qualitative information

2. communicating treatment options to the patient

3. exercising human judgment based on the costs, risks, and potential payoffs of the possible treatment options.



# T1-Q4: Precision & Recall

A blood test for cancer was evaluated on 10 patients who were known to have cancer and 20 patients who were known to be free of cancer. The blood test falsely identified 2 of the 20 cancer-free patients as having cancer and correctly gave a negative test result for the other 18 cancer-free patients. 2 false positives out of 20 tests of patients who are actually cancer free is a *﻿﻿﻿﻿﻿﻿﻿﻿﻿false positive rate* of 10%.
The same test falsely gave negative test results for 3 of the 10 patients with cancer and correctly gave a positive test results for the other 7 patients known to have cancer. 3 *false negatives* out of 10 tests of patients with cancer is a 30% *false negative rate*.
What is the test’s precision, or the test's ability to avoid falsely identifying a patient as having cancer?
What is the test's recall, or the test's ability to find all the patients with cancer?

# T1-A4: Precision & Recall

                21 tested neg     9 tested pos
20 with cancer: TN=18             FP=2
10 cancer-free: FN=3              TP=7

- Precision = TP / (TP + FP) = 7 / (7 + 2) = 7 / 9  = 77.77 %
- Recall    = TP / (TP + FN) = 7 / (7 + 3) = 7 / 10 = 70.00 %


