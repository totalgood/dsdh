# 1: Spreadsheet Data Science

<aside class="notes">
    Welcome to the second lesson of the Data Science for digital health course at UCSD Extension.
    This is one of the required courses in the Digital Health certificate.
    I'm Hobson Lane and I will be your instructor for this lesson.
    I'm excited to show you today how you can actually apply data science to your own life or to patients in the healthcare system.
    Today you will get to build your first predictive model.
    All you will need to use the techniques in this lesson is a modern spreadsheet application like Libre Office, Open Calc, or Google Sheets.
    The assignment for this lesson will allow you to try your hand at data science for yourself.
</aside>

# 2: Agenda

- Advantages: When to use a spreadsheet
- Applications: DIY, Healthcare
- Data: Datatypes
- Database: Relational database , Graph database (nosql)
- Spreadsheet statistics: Sum, mean, standard deviation
- Spreadsheet visualization: Scatter plots & histograms
- Spreadsheet modeling: Linear regression, Classification

<aside class="notes">
    - In this Lesson you will first learn about some reasons why you might use spreadsheets for data science and when you might want to use a programming language like python instead.

    - Next you will hear the stories of DIY doctor-yourself individuals using spreadsheet data science to improve their health.
    In some cases these citizen science heroes are saving lives by sharing their discoveries with the global open source community.

    - Once you are motivated by these inspiring stories of healthcare democratization, you'll dig into the nitty gritty of the data types you'll encounter when working with healthcare data.

    - Then you'll see where this structured tabular healthcare data normally lives, in a database.
    And you learn how data is normally retrieved from these databases whether they be on your phone, on the servers at your office, or in the "cloud."

    - Then you'll learn how to convert these various real world datasets into a form appropriate for data science, whether you downloaded your data from the web, a database, or servers your office.
    Then you will see how having your data in this form enables your spreadsheet to produce some informative plots and visualizations.

    - You'll compute some descriptive statistics in a spreadsheet with a simple but useful healthcare dataset.
    And you'll see how these **descriptive** statistics can be used as **predictive** statistics.
    This will help you create your first data science model that you can use in the real world, at home, in a research lab, or even in a clinical setting.

    - Finally you'll wrap up this lesson by extending your statistical data science model to become a machine learning model.
    Yes, even machine learning is possible with a spreadsheet of data.
    All you need is a few columns of numerical data that you are interested in.
</aside>

# 3: Spreadsheet Advantages

Approachable
Universal
Transparent
Automatic variable names (“A1”, “B3”)
Data + Code + Graphics
Killer feature: automatic filters

<aside class="notes">
    Spreadsheets are approachable for everyone in your organization and perhaps everyone in your family.
    I saw my first spreadsheet as a preteen.
    An accountant asked more my help building a formula in his bookkeeping spreadsheet for a healthcare organization.
    You know you have an approachable and intuitive UX when a 13 yr old can use it without reading an instruction manual.

    And because they are so approachable, spreadsheets are everywhere.
    They are ubiquitous.
    If you have access to the Internet you can use Google sheets in any modern web browser. And it's free, sort-of.
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

# 4: CRISP-DS: CRoss Industry Standard Process for Data Science

1. Data Understanding
2. Data Preparation
3. Modeling
4. Evaluation
5. Deployment
6. Domain Understanding

<aside>
    When you talk about CRISP, what's the first thing that comes to mind?
    Probably CRISPR, the gene editing technique developed by [Jennifer Doudna][Doudna].
    Data Scientists, however, think of something different.

    Two decades ago, Rüdiger Wirth and Jochen Hipp published a paper describing the 6-stage CRISP data mining process.
    The CRISP data mining methodology has been taught in universities and corporate training programs ever since.
    It even survived the terminology change as from data mining moved from industry into the laboratory and was rebranded as data science.
    CRISP-DM is now the _de facto_ mental model for Data Science.
    Technology has advanced much faster than this mental model.
    With automatic machine learning tools like H20ai or even Scikit-Learn Pipelines, most of this process can be automated.
    Two decades ago, Rüdiger Wirth and Jochen Hipp published a paper describing the 6-stage CRISP-DM data mining process.
    It has been taught in universities and corporate training programs ever since even as emphasis evolved from data mining to data science.
    It is now the de facto mental model for Data Science.
    Technology has advanced much faster than this mental model.
    With automatic machine learning tools like H20ai or even Scikit-Learn Pipelines, most of this process can be automated.

    [Wirth]:
    [Doudna]: https://en.wikipedia.org/wiki/Jennifer_Doudna "Jennifer Doudna"
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

# 5: Healthcare Applications

Patient “intake”
Operations management
Insurance actuarial tables
Presentation (visualization)
Cooperative analysis

<aside class="notes">

    In addition to the personalized medicine and DIY uses for spreadsheet data science, spreadsheets are often used to manage healthcare data in a professional setting.
    EHR systems are replacing the use of spreadsheets in Europe and the US but in many international communities, spreadsheets are still widely used for patient data.
    Spreadsheets nicely compartmentalize ones data and separate it from other patients' data.
    When you incorporate clinical data into a normalized database management system or EHR system you greatly expand the value of the data but add significant complication and privacy challenges.
    You only have to look at the numerous EHR systems that have been attempted and failed in the US to see this.

    Even in the US spreadsheets are still the tool of choice for many healthcare organization administrators, executives, managers, and accountants.
    Financial and quality of care models are often first drafted in spreadsheets before they are handed over to data scientists for further analysis.
    And data scientists will often export their models back into spreadsheets for dissemination among colleagues and management.
    Clinical personnel often find the visualization and data manipulation features of spreadsheets sufficient to meet their needs.

    In a clinical setting the transparency and approachability of spreadsheets is a big advantage.
    It can often be the difference between finding and dealing with missing or erroneous data before it's too late.
    The more eyes that are looking at a dataset the more likely errors will be caught.
    However, in later lessons you'll learn how to augment human eyes with automatic anomaly detection algorithms.
    This is your only option when your dataset grows too large for manual human inspection.
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

<aside class="notes">
    You have likely encountered several different data types in the healthcare industry.
    The most straightforward type of data is the tabular data that we have talked about so far.
    This is the way you will want to arrange your data in order to do data science, especially spreadsheet data science.
    Tabular data can contain text or numerical values and in some cases will contain markers for missing or erroneous data.
    You will learn later how to convert these text values into numerical values for data science.

    When you have multiple tables that are related to one another you can store that data in a relationsl database.
    Big pharmaceutical companies and insurance companies do not limit themselves to spreadsheets to store their data.
    You'll learn more about this "industrial strength" data storage tool in later slides.

    Another kind of data you have likely run across in the past is imagery.
    This includes radiology images like X-rays, MRI (Magnetic Resonance Imagery), CAT scans, and dermatology photographs.
    You can see two examples of a visible light photograph of a wound in an ankle here.
    There is also an X-ray image of an ankle for comparison.
    As a data scientist you will learn to see the numbers behind these pictures.
    In later lessons you will see how to extract these numbers, or features, using machine learning, or even deep learning.

    Time series are fourth kind of data you may have seen.
    Any data records that are sequenced according to a date or time stamp are called time series.
    This is because the series of time-ordered records must be kept in order and cannot be shuffled without losing some of their predictive value.
    You will learn about time series in the lesson on operations management data science because many healthcare system records are recorded in a log that includes date and time.

    If you combine image data and time series data you get an image time sequence or a video.
    Videos are often used in psychology interviews and sometimes in physical therapy, when a persons body language and expressions are important to evaluate health or recovery.
    Video data is some of the most difficult to work with in Data Science.
    It is possible, but this advanced topic is outside the scope of this course.

    Finally, there is unstructured data, like the notes a doctor takes while making the rounds.
    EHR systems have improved the amount of structure in clinical medical records by adding checkboxes and pulldown menus for doctors to select from.
    But very often the appropriate code or checkbox is not provided.
    This data ends up being written down as comments or descriptions in a natural human lanugage like English or Spanish.
    I helped a company called Manceps in Portland Oregon develop a Data Science pipeline for clinical medical records.
    In particular, Manceps built a system for summarization of the entire medical history of each patient in their client's system.
    This enables doctors to more quickly evaluate the pages of text that they must review.

    Another valuable source of unstructured data is the text in medical journals.
    Medical journal articles contain a wealth of information about genetic markers and potential drug interactions and side effects.
    I'm helping a company called Canvas.Health mine medical journals to extract genetic information that can be helpful in diagnosing rare diseases.
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

<aside class="notes">
    Healthcare applications like Electronic Health Record (EHR) systems store data in what's called a relational database.

    You can think of a relational database as a sequence of tabs in a spreadsheet.
    For example you might have a table in one tab that contains patient intake data like height and weight and blood pressure, like the Patient table shown here on the right.

    In another tab named "IQ" you might store historical data about IQ test results.
    Let's say you are trying to establish a baseline to measure the progression of diseases like Alzheimer, Dementia, or perhaps neurological damage from stroke or trauma.
    In a spreadsheet application you could connect these two tables with the patient ID variable that you have recorded in both tables.

    This is called a relationship.
    A relationship between tables goes from a foreign key in one table to a primary key in another table.

    In a spreadsheet you would use a "VLOOKUP" function to retrieve a particular value in your spreadsheet tab.
    VLOOKUP mean "value lookup".
    In red you can see an example VLOOKUP command.
    The first argument of the VLOOKUP function is A2, this is the cell location in the Patient table to the right that contains the PatientID value that you want to look up in the IQ table to the left.
    The second argument of the VLOOKUP function is the range of values were the patient ID and the value you are looking for can be found.
    You are looking for a value in the range A3 to D501 in the which contains all the PatientID, Gender, Age and FIQ
    In this command the number 4 as the last argument means that you want to retrieve the value in the 4th column of the data range that you specified.
    This is the FIQ of the patient because we specified a range that includes the four columns PatientID, Gender, Age, and FIQ.

    In a relational database system we have a query language called S Q L or sequel.
    S Q L stands for Structured Query Language.
    The sequel command to retrieve that same value is a bit clearer and less likely to retrieve the wrong value.
    The sequel command is "SELECT FIQ from IQ where PatientID = "A".
    The sequel language was designed to be readable like English.

    Like spreadsheets, sql databases are everywhere.
    If you have a smartphone in your pocket, you have many relational databases running inside of it using an opensource RDMS (relational database management system) call sqllite.
</aside>

# 8: NOSQL Database (Graph Database)


<aside class="notes">
Deep, dynamic relationships between objects are often stored in a graph database.
This kind of database is often called a NOSQL database because they do not use the SQL language.
Graph databases use graph query languages to perform logical reasoning about the relationships in a table.
An example of a graph database is the information about all the connections between people in a social network database.

In healthcare these kinds of deep databases are rarely required.
But in some cases, such as when modeling the interaction of people to monitor the spread of communicable diseases in epidemiology, graph databases might be more efficient than a relational database.
Nonetheless, you will rarely use graph databases in a healthcare setting so you will not be required to work with them in this course.

</aside>

# 9: Data Dichotomies

Continuous vs discrete
Categorical vs numerical
Cyclical vs ordinal
High-D, Low-D
Structured (Labeled) vs unstructured
Deterministic vs Chaotic/Random (Noise)
Big (“out of core”) vs small

<aside class="notes">
    The first distinction between different kinds of data you will learn is continuous vs discrete.
    A continuous variable can take on a fractional value and is not limited to discrete steps in magnitude.
    You might measure someone's height in a discrete number of inches, but height itself is a continuous variable.
    Your patient can grow half an inch and your data science statistics will be able to take that into account.

    This distinction between continuous and discrete values may lead you to think about categorical values.
    Gender and ethnicity are examples of categorical variables.
    These can be encoded as answers to yes or no questions, such as: is the patient male or not, is the patient female or not, is the patient transgender or not.
    This means that a data science model will treat categorical variables like gender as a set of related binary values, 1 or 0, for yes or no answers to questions like these.
    You will work with a categorical variable for gender at the end of this lesson and in the assignment for this week.

    Some discrete values have a natural order, like small, medium and large; or mild, moderate, and severe.
    These are called ordinals or ordinal variables because they have an order.
    Your job as a data scientist is to convert these to numbers that are faithful to this order, such as 1, 2 and 3 for small medium and large.
    However, these values may not always have an obvious order, like Short, Tall, Grande, Venti, and Trenta
    In such cases it is best to treat these unknown discrete text values as categorical.
    The statistics will show you what the order for these values should be based on their relationship to the target variable.
    And this will help your model deal with potential nonlinearities better, in case the value needs to change more when go from Small to Medium than when going form Medium to Large.

    One of the most important qualities of a variable for data science is its dimensionality.
    This gives you an idea for how much information it might contain.
    Any one of the dimensions of a multi-dimensional variable may contain a value that is predictive of your target variable.
    Some examples of high dimensional data include images, ekg traces, and gene sequences.


    Not all ordinal variables should be treated as discrete integer values like 1, 2, 3 real values.
    In some cases these variables wrap around in a cycle.
    Obviously Sunday is before Monday and after Saturday, but you should not use the number 1 to represent Saturday and 2 for Sunday, etc. Because if Friday is the last day of the week it might have a value of 7 which would be much larger than Saturday, the Day that follows it.
    There is not way to arrange the integer values so that the ciclical nature of dates and days of the week are accounted for. So these should usually be converted to categorical binary variables like "is a saturday" or "is a sunday" or "is a friday".
</aside>

# 10: Data File formats

Text files (CSV, TSV, JSON, TXT)
Compressed (ZIP, GZ)
Binary files (XLS, PDF)
Images (PNG, JPG, TIF)
Web pages (HTML)
Databases (SQL, NOSQL, HDF)

Hint: check out “Pandas” and the `pandas.read_csv()` function

<aside class="notes">
    These different kinds of data are often stored in different file formats.
    You will import and process these files, either with python or with your spreadsheet program.
    For example, CSV, TSV, and TXT files can usually be imported directly into a spreadsheet.
    JSON files are a more general format that is more suited to being processed by languages such as python.
    You will learn how to deal with such files later in the course.

    Compressed files such as those with the ZIP and GZ extension must be extracted or expanded by an application within your operating system.
    Python packages can usually handle these formats directly.
    But if you want to use your spreadsheet for data science on these kinds of files, your will have to extract them first.
    Similarly binary file formats like PDF or XLS mush be loaded by the appropriate application and then converted to a more machine-friendly version like TXT or CSV.
    The other formats listed here, like HTML, HDF, JPG, and TIF, may come up in your healthcare data science journey, but you will need to rely on python to help you process them.
    And in some cases you may need to solicit the assistance of a developer to help you process these files efficiently.
<aside>

# 11: Data types

Continuous: numerical values like height, weight, blood pressure, temperature
Categorical: gender, eye color, disease names
Natural language: symptom descriptions, medical procedure descriptions
Sequence: genome, DNA, RNA, protein, chemical pathways
Time series: treatment timelines, hospital records, EKG/EEG recordings)
Geographic: epidemiology, maps of clinic locations
Imagery: X-rays, MRI slices, CAT scan slices, photos of skin abnormalities

<aside class="notes">
    Within a data science dataset or table you are likely to encounter many different kinds of data points or values.
    Continuous values are the most straight forward.
    These are values like height, weight, blood pressure, and body temperature.
    Continuous values can take on fractional values and are not limited to discrete, stair-step jumps in value.
    Categorical values like gender, eye color, and disease names will also be common.
    You will encounter these as text values within your spreadsheet.
    It will often be a challenge for you to consolidate multiple different spellings of a particular value to ensure that your data science statistics are accurate.
    Natural language data points are another kind of text data you will sometime see.
    When your text doesn't have a limited number of possible words or terms that are used for it, then it is called natural language because it must be processed using natural language processing tools.
    The book _Natural Language Processing in Action_ by Manning Publishing is an excellent guide to these techniques and we will use some of the examples from that book later in this course.
    Sequence data includes DNA, RNA and chemical pathway sequences.
    Time series data can include datasets like treatment timelines and hospital records that contain a timestamp or date column.
    Geographic data includes map and location information often used in public health studies.
    Imagery includes X-rays, MRIs, CAT scans, and photographs of the skin.
<aside>

# Time Series

year, month, day
  is it a weekend or a weekday?
  is it summer, winter, spring or fall
hour
is it night or day?
is it within business hour?
is it rush hour or lunch hour?

<aside class="notes">
    <aside>
# 12: Geographic data

<aside class="notes">
    Another kind of data that you encounter among the spreadsheets and databases of healthcare is geographic data.
    This can be represented as a pair of latitude and longitude values in a spreadsheet.
    Or it might be represented as a categorical variable like zip code, city, county, state, or even country.
    Converting an address or zip code to latitude and longitude information is called geocoding.
    Geographic data  is valuable for data science in the modeling of epidemics and public health.
    You will learn techniques like geocoding in a later lesson on public health or population health.
    You will also learn how to extract import new features from geographic data, like the distance to the hospital or clinic for each of the latitude and longitude data points in your database.
    You will work with automotive accident records to get a feel for the variables that affect emergency room statistics at hospitals across the country.
</aside>

# 13: Sequence Data

Self-service genetic testing (23andme)
Prenatal screening (Counsyl)
Pre-exposure allergy prediction
Asthma anticipation
Resistance to disease (AIDS, Malaria, West Nile, Ebola)

<aside class="notes">
    We discussed time series data earlier.
    Sequence data requires the same processing techniques that you will use for time series data.
    You will need to maintain the order of the sequence in order for the data science statistics to be meaningful.

    Nucleotide, amino acid, and protein sequences are all example of sequence data.
    Processing this kind of data is one of the skills of a microbiologist or a bioinformatics engineer.

    Genomic data is commonly used by companies like Counsyl, Illumina, and 23andme to predict various heridtatry diseases.
    Genomics, aminomics, and proteomics can be used in data science models that predict things like allergies and asthma, without exposing patients to stressful or potentially life threatening irritants.
    Gene sequence data can also be used in the field of epidemiology to predict resistance to disease and potentially identify gene therapies to increase disease resistance.
</aside>


# 14: Weight Guesser Example (Patient Intake)

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

14: Weight Guesser Dataset

Height
Weight
Gender

<aside class="notes">
    Take a look at this example dataset for our weight guessing model.
    Notice that we have four columns one for PatientID and others for Gender, Height, and Weight.
    Now an ID like PatientID in this table is not useful for data science.

    An ID value is unique for every record in our table, so there will not be any patterns in this value that the machine can use to predict the weight of our patient.
    The Gender, Height, and Weight, columns, however, contain the information we're looking for.
    The gender and height data will have some relationship with the variable we are trying to predict.
    You will not always have an intuition about which columns or variables in your dataset are important.
    You may not even know what they mean, like the presence or absence of a particular chemical or genetic marker.
    That's OK.
    As long as you can convert the data into a meaningful numerical representation, the statistics of the data will tell you everything you need to know.
    The machine will find the patterns that relate your variables to each other.

    That brings us to another concept, the concept of the target variable or the dependent variable.
    It is called the target variable because your model is trying to hit the target values in your training dataset as closely as possible.
    This target variable is the value that you want your model to predict or output.
    In our case we have chosen the Weight measurement as our target variable.
    This target variable can also be called a dependent variable because it often depends on the values of the other variables in the table.
    These other variables are then called the independent variables or feature variables.
    They are also called features or attributes because they describe the objects in our database, in our case they are attributes of the patients we have examined.

    But this selection of target and feature variables is often arbitrary.
    For this simple dataset that has 3 variables, we could potentially create 3 different data science models.
    For example we might want to predict gender as our target variable using height and weight as our feature variables.
    This could be useful if in some cases we are missing this piece of information in our database and we want to interpolate it based on the other information in our database.

</aside>

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

    Medtronics engineers generously decided to license the open source software to incorporate it into their system.
    But hackers were able to find security vulnerabilities in Medtronics implementation in 2018 and Medtronics was unable to update the software to protect users so FDA recalled several models.

    The DIY systems are not vulnerable to the hacks, and are now the only affordable option for many diabetics.

    So if you want to take your Data Science and spreadsheet formulas to the next level you'll need to learn a little programming.
    Python is a lot like the visual basic scripts you are used to in using in spreadsheets, only Python is a lot more understandable and powerful.

</aside>

### References

[Diyps.org/about/dana-lewis/](https://diyps.org/about/dana-lewis/)




