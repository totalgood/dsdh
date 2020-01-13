# 1: Spreadsheet Data Science

# 2: Agenda

# 3: Nice Features

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
- [Dana Lewis insulin pump](https://medicalxpress.com/news/2019-06-hacking-diabetes-people-insulin-alternative.html)


