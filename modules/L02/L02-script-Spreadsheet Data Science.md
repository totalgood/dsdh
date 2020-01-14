# 1: Spreadsheet Data Science

# 2: Agenda

# 3: Spreadsheet Advantages

Approachable
Universal
Transparent
Automatic variable names (“A1”, “B3”)
Data + Code + Graphics
Killer feature: automatic filters

<aside class="notes">
    Spreadsheets are approachable for everyone in your organization.
    I was barely 13 when I saw my first spreadsheet and helped an accountant build his first formula in Lotus 1-2-3.
    You know you have an approachable and intuitive UX when a 13 yr old can use it without reading an instuction manual.

    And because they are so approachable, spreadsheets are everywhere.
    They are ubiquitous.
    If you have access to the Internet you can use google sheets in any modern web browser. And it's free, sort-of.
    By tying yourself to the Google ecosystem you are helping them ensure that their ads will reach your eyeballs.

    If you need to work in an isolated environment, where no one, not even google can see what you're working on, there's open source for that.
    You can use free, open source tools like `pyspread` or Libre Office Calc to build even more sophisticated models without any of your data or your patient's data leaking out onto the internet.

    Ubiquity is a big deal in high security environments like hospitals and nuclear facilities and suboena vaults.
    In secure environments, often computers are air-gapped from the internet to reduce the "attack footprint", reduce the vectors of infection with malware.
    So if you need to work with data, you're stuck with whatever antiquated spreadsheet application, like Microsoft Excel, is installed on the machine.
    It can take months, if not years for IT and security to install requested software on your machine.

    Spreadsheets are transparent.
    You can scroll around and find any value you're looking for.
    If you want to understand how a particular number was calculated, you can click on a cell and examine the formula.

    And you can find any variable referenced in the formula using the automatic grid-reference variable names like A1 and B3.
    These are geographic coordinates that map well to the human mind's mental model of where your data is within your spreadsheet.

    When you finish with your calculation or presentation you can email the sheet to your colleagues and they can see exactly what you did.
    A spreadsheet contains all the data and visualizations and formulae that you used to produce your results.
    If only the medical system could e-mail us our blood test history in a spreadsheet.
    Actually, it won't be too long when this may be possible, as GDPR and EHR regulations in the US catch up with those in Europe and Australia.

    Finally, my favorite feature about spreadsheets is the automatic filters.
    You can quickly see how many different values are in a spreadsheet by applying an automatic filter or using the pull down menu in the heading of modern spreadsheets.
</aside>

# 4: DIY Spreadsheet Data Science

- Fitness: step counters, heart rate monitors
- Psychology: Stress, anxiety, and depression
- Sleep: (CPAP data streams, smart watches)
- Home EEG: behavioral feedback
- Home EKG: Heart disease (smart watches)
- Parkinson disease medication pump
- Insulin pump hack

<aside class="notes">

The rise in citizen science has enabled people around the world to contribute to data science projects like environmental conservation and climatology.
Similarly the "Quantified Self" movement created a global community of citizens monitoring their health and well-being.
In many cases people are contributing their data to citizen science projects or even hacking  their own healthcare devices and treatment.

With modern wearable devices, you can count your steps, monitor your heart and breathing rate.
With do it yourself EKG equipment you can monitor the electrical signals emanating from your heart to detect arythmia and other symptoms of a pending heart attack.
With behavioral feedback hats you can even monitor your brain waves similar to an EEG or electro encephelogram.
Most smart watches will monitor your sleep patterns detecting if you are dreaming within the REM sleep stage.
Smart watches can also detect if your body has reached the deep sleep state that washes your brain of toxins and metabolites that build up over time.

Smartphones are becoming a medical device.
The accelerometers and gyroscopes in the modern smartphones not only track your movement but can also monitor your health.
They can detecting harmful biomechanical patterns in your movement.
And they can help you optimize the pace of your exercise regimine.
And cellphones are being used for therapy and companionship by the millions of users of chatbots and wellness apps like Replika, Xiaice, Woebot, Youper, Breath, Calm, and Mindcurrent.
Often this data is provided in a downloadable spreadsheet that you can use do spreadsheet data science on yourself.

In some cases people are even using Data Science to diagnose and treat serious illnesses like heart disease, diabetes, and parkinsons disease.
If you want to see an inspiring sotry of a woman treating herself for parkinsons look up Jasmine Sturr and her Parkinsons Phenome project on YouTube.
She has juvenile onset parkinsons disease and has embarked on a crash course in medicine and data science to extend her life and maintain her quality of life as long as possible.

Another disease where technology is being rapidly pushed forward by "agressive patients" is diabetes.
Search for Dana Lewis on DuckDuckGo to learn more about this community of do-it-yourselfers building and hacking insulin pumps.
Her insuling pump was the first to automatically adjust the dosage rate based on feedback from a wearable glucose monitor.
And her feedback algorithm was 50% more reliable and accurate than what the pharmaceutical companies could come up with after years of research so they licensed her software rather than trying to build their own.

Even for these serious illnesses, "agressive patients", as doctors call them, are using spreadsheets to extend their lives and improve their quality of life.
Spreadsheets are helping to democratize medicine.

So in this course you'll do your first data science in spreadsheets, just as these DIY pioneers and hackers of medicine did.
And, like them, hopefully this taste of data science will inspire you to learn more and quickly graduate to the more advanced tools in the Python ecosystem that we'll cover in the remainder of the course.

</aside>

### References

- [Jasmine Sturr parkinsons phenome project](https://youtu.be/XeGLPWfg9qQ)
- [Dana Lewis ted talk](https://www.youtube.com/watch?v=kgu-AYSnyZ8)
- [Dana Lewis insulin pump](https://medicalxpress.com/news/2019-06-hacking-diabetes-people-insulin-alternative.html)

# Healthcare Applications

Patient “intake”
Operations management
Insurance actuarial tables
Presentation (visualization)
Cooperative analysis

<aside class="notes">

    In addition to the personalized medicine and DIY uses for spreadsheet data science to manage your own healthcare, spreadsheets are often used to manage clinical records.
    EHR systems are replacing the use of spreadsheets in Europe and the US but in many internation communities, spreadsheets are still widely used for patient data.
    Spreadsheets nicely compartmentalize ones data and separate it from other patients' data.
    When you incorporate clinical data into a normalized database management system or EHR system you greatly expand the value of the data but add significant complication and privacy challenges.
    You only have to look at the numerous EHR systems that have been attempted and failed in the US to see this.

    Even in the US spreadsheets are still the tool of choice for many healthcare organization administrators, executives, manageers, and accountants.
    Financial and quality of care models are often first drafted in spreadsheets before handed over to data scientists for further analysis.
    And data scientists will often export their models back into spreadsheets for dissemination among colleagues and management.
    Clinical personnel often find the visualization and data manipulation features of spreadsheets sufficient to meet their needs.

    In a clinical setting the transparency and approachability of spreadsheets is a big advantage.
    It can often be the difference between finding and dealing with missing or erroneous data before it's too late.
    The more eyes that are looking at a dataset the more likely errors will be caught.
    However, in later lessons you'll learn how to augment human eyes with automatic anomaly detection algorithms.
    This is your only option when your dataset grows too large for manual human inspection.
</aside>

Tabular data
Relational data
Hospital, insurance, and pharmaceutical company databases
Images
X-Rays, MRI files, dermatology visible images
Time series
Hospital records, log files, audio
Image time series
Video of patient interviews (Awakenings)
Unstructured data (natural language):
Doctor & nurse notes

<aside class="notes">
    So far you've only seen tabular data in our discussion of the various
</aside>



# Patient Intake Example

<aside class="notes">

To get a feel for the advantages and disadvantages of spreadsheets you're going to work through an example on some real data.
You may have seen the weight-guessing machine or magician at your county fair.
But did you know that the magician is using data science to guess your weight?
If it's a machine guessing your weight then you can legitimately call it a machine learning system.

All joking aside, a weight guessing can be valuable in the clinical setting as well.
Imagine you have some historical patient records that are missing weight information, and you'd like to improve your data science model of your patient's diagnosis?

Or imagine that you just want to use a weight prediction to help you detect outliers or anomalies that might be indicative of a disease.
Outlier data points are measurements that are outside the normal range of measurements that you'd expect to see.
If you just set your range based on all the weights of humans around the world, you'd miss a lot of potentially diseased people.
If you just take into account a person's height and gender you can narrow your normal range quite a bit.
It's become so useful at diagnosing disease that the model has been incorporated into what's known as the BMI or Body Mass Index.
This is a number that tells a physician how far your weight is from the normal range expected for someone of your height.

Incidentally, to prepare this dataset I ended up using python to shuffle the records because my spreadsheet application doesn't provide a shuffle function.
In python this is a simple one-line command and takes milliseconds to run.

</aside>

# 6: Kinds of Datasets

Tabular data
Relational databases (SQL)
Hospital, insurance, pharma, etc
Images
X-Rays, MRI, CAT, dermatology
Time series
Hospital records, log files, audio
Image time series
Video of patient interviews (Awakenings)
Unstructured data (natural language):
Doctor & nurse notes

# 7: Spreadsheet Tabs vs Relational Database Tables

Relational Database captures relationships
Structured Query Language (SQL):
`SELECT IQ.Age FROM Patient WHERE Patient.Height > 65`

# 8: NOSQL Database (Graph Database)

Deep, dynamic relationships

# 9: Data Dichotomies

Continuous vs discrete
Categorical vs numerical
High-D, Low-D
Structured (Labeled) vs unstructured
Deterministic vs Chaotic/Random (Noise)
Big (“out of core”) vs small


# Insulin Pump Hack

1973: wearable insulin pump (Dean Kaman)
2003: wearable CGM (glucose monitoring)
2013: Dana adds #DIYPS to #WeAreNotWaiting
2015: Dana Lewis hacks an artificial pancreas
2017: Medtronic integrates Dana's technology
2018: Medtronic notifed of security vulnerability
2019: FDA recalls MiniMed insulin pumps

<aside class="notes">

Now that you know all the cool Data Science you can do with spreadsheets you're ready to take it to the next level.
Do you remember Dana Lewis and her insulin pump hack from the beginning of this lesson?
Dana wasn't satisfied to merely limit her data science to a desktop spreadsheet that she used to track her glucose levels.
First she wrote software to increase the volume and improve the precision of her glucose alarm by wirelessly connecting to her CGM.
Then in 2014 her friends in the #DIYPS community helped her reverse engineer the electrical interface on her Medtronic insulin pump and glucose monitor.
After months of testing her software on a Raspberry Pi she eventually used it on herself to create the first field-tested artificial pancreas.
A Raspberry Pi is a single board computer about the size of a stack of 50 business cards that can run for hours on a portable battery pack.

Medtronic engineers generously decided to license the open source software to incorporate it into their system.
But hackers were able to find security vulnerabilities in Medtronics implementation in 2018 and Medtronic was unable to update the software to protect users so FDA recalled several models.
The DIY systems are not vulnerable to the hacks and are now the only affordable option for many diabetics.

So if you want to take your Data Science and spreadsheet formulas to the next level you'll need to learn a little programming.
Python is a lot like the visual basic scripts you are used to in using in spreadshets, only Python is a lot more understandable and powerful.

</aside>

### References

[Diyps.org/about/dana-lewis/](https://diyps.org/about/dana-lewis/)




