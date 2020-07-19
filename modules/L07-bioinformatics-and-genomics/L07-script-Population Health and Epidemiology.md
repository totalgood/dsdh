# Population Health and Epidemiology

# Epidemiology

Simulations are a special kind of data science modeling, typically used to forecast spatiotemporal data.
A python exercise in simulation of an epidemic.

MIT Intro to Computational Thinking [Problem Set 4: Simulating the Spread of Disease and Bacteria Population (ZIP)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/assignments/PS4.zip)


# Spatiotemporal data

Epidemology data often has

- a place (location in space)
- time (when the data was observed)

This adds 3 dimensions (latitude, longitude, time) to data that is already probably high dimensional.
For most predictive models these discretized locations and and times often become additional dimensions.
Predictive models must deal with extremely high dimensional features.

::: note

Epidemiology and populaiton health data is usually recorded over time and the geographic information is critical to the model.
A GIS system is often used to store and visualize spatiotemporal data.
Layers are added/modified over time to show the evolving geography of a phenomenon.
The end result is a "spy satellite" movie.
The past history of all the events nearby are all relevant feature for the prediction of what is about to happen at a particular location at a particular time.

:::
