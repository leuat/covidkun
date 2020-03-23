# covidkun
Covid-kun is a small python script that analyzes fresh covid-19 data and predicts a model of infection growth for individual countries. Data are downloaded with each use.

The script basically uses a 2-parameter exponential model to perform a brute-force 2D chi^2 fit with data from the requested country, then extrapolates infectiom data from this model. 

usage: 
  ./covidkun.sh US
  ./covidkun.sh Norway
  ./covidkun.sh "United Kingdom"
  
  etc

