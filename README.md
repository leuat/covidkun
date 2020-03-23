# covidkun
Covid-kun is a small python script that analyzes fresh covid-19 data and predicts a model of infection growth for individual countries. Data are downloaded with each use.

The script basically uses a 2-parameter exponential model to perform a brute-force 2D chi^2 fit with data from the requested country, then extrapolates infectiom data from this model. 
<br>
usage: parameter is a query, any country name containing the query will be included in the count and estimate <br> 
  ./covidkun.sh US<br>
  ./covidkun.sh Norway<br>
  ./covidkun.sh United<br>
  
  <br>
  etc<br>

