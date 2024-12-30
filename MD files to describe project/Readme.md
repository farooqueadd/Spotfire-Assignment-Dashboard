<h1 style="color:#00d6b4;">Spotfire-Assignment-Dashboard</h1>

Dashboard link: https://spotfire-next.cloud.tibco.com/spotfire/wp/OpenAnalysis?file=1773e29b-62ce-4c03-add9-4bd5b5087637
<br>*please make sure to trust scripts to see js script for KPIs and other python datafunctions


<h2 style="color:darkcyan;">Objective</h2><br>
Analyse COVID-19 and mortality based on healthcare spending and vaccination across multiple countries , focusing details on USA and India data from COVID-19 Data API.<br>
<OL>
<li>	Analyze Global COVID-19 Impact:
    <OL>
    <li>Visualize total cases, deaths, recoveries, and vaccinations at a high level.</li>
    <li>Compare mortality rates across different countries.</li>
    </OL>
</li>
<li>	Understand Healthcare Correlation:
    <OL>
   <li> Examine the relationship between healthcare spending per person and mortality or death rates.</li>
    <li>Identify if countries with higher healthcare expenditure have lower death rates.</li>
   </OL>
</li>
<li>	Identify Trends and Outliers:
    <OL>
    <li>Evaluate population vs. death rate patterns through scatter plots.</li>
      <li>Forecast for next 5 years</li>  
        </OL>
</li>
    
<li>	Geospatial Distribution:
    <OL>
    <li>Map COVID-19 cases, vaccination rates, or healthcare facilities by country.</li>
    <li>Highlight hotspots and regions with higher/lower healthcare investment.</li>
        </OL>
</li>
</OL>

<h2 style="color:darkcyan;">Dashboard Snapshots</h2><br><strong>Tab 1: Covid Mortality and Healthcare </strong></br>
<img src="C:/Users/Farooque Jamal/Documents/Projects/AIQ/Images/Page 1.png" alt="Alt Text" width="800"/>
<br><strong>Tab 2 : EDA </strong></br>
<img src="C:/Users/Farooque Jamal/Documents/Projects/AIQ/Images/page 2.jpg" alt="Alt Text" width="800"/>

<h2 style="color:darkcyan;">Data </h2><br>
Data is loaded from <br>
<OL>
<li> COVID-19 Data API
    <OL>
        <li>CountrywiseCovid19<br> Countrywise data for selected countries (India,USA,Brazil,Germany,Japan,South Africa,Saudi Arabia) </li>
        <li>Statewise Covid19<br> Statewise data for India and USA </li>
    </OL>
</li>
<li> World Bank API
    <OL>
        <li>WorldBankData <br>Year wise economic indicators for {selected countries}</li>
       
   
</li>
<li> OpenStreetMap (OSM)
     <OL>
        <li>Healthcare facilities <br> hospitals and clinics for {drop down selected states} for India and USA </li>
       
     
</li>
<li> Excel data embedded
   <OL>
        <li>country_code_mapping <br> Country mapping for API data and maps </li>
       
    
</li>

</OL>

<h2 style="color:darkcyan;">Model</h2><br>
CountrywiseCovid19 api data table is left joined with country_code_mapping excel data.<br>
-This is  one to one relationship<br>
Other API data tables are mapped by editing table relationships on state or country.<br>
-All of this are many to one relatiosnhip or vice verca<br><br>
Tranformations used: Filter rows, exclude columns

<h2 style="color:darkcyan;">Custom R/Python functions</h2>

Mainly used for connecting data from various API. Used only built in packages like http.client, json etc.
Data is manipulated to convert from JSON to spotfire row major column type tables.
Tried Predicitons using sklearn but sklearn is not available by default to import, so used spotfire's defualt foreacsting. 

<h2 style="color:darkcyan;">Architecture of the dashboard</h2>

User interactions
<li>Markings are used to filter data from main visual </li>
<li>Markings used for loading api data online</li>
<li>Filter used for healthcare facilities</li>
<li>On EDA all filters as included which have a different filtering scheme to seperate from main analysis</li>




Big Picture
<li>Get data from various public API get requests, made time consuming api on demand when user interacts.</li>
    <li>Joined neccessary tables</li>
        <li>Tables whihc doesnt have a unique id or clear join natures are virtually joined using relationships.</li>        

<h2 style="color:darkcyan;">Spotfire infrastructure</h2>

<li>Spotfire Analyst : desktop client for dashboard development, data manipulation and advanced analytics</li>
<li>Spotfire Web Player – wEB based client that allows users to interact with dashboards through a browser.</li>
<li>Spotfire Server – Server where spotfire is hosted.The central component that manages users, licenses, and access control.</li>
<li>Data Connectors – Facilitate connections to databases, cloud storage, and big data systems.</li>
<li>Spotfire Node Manager – Handles scaling by distributing workloads across multiple nodes.</li>



Scaling Consideration
<li>Vertical Scaling: Increase CPU, RAM, and storage of the existing Spotfire Server</li>
<li>Horizontal Scaling: Add more Spotfire Web Player instances or Spotfire Servers to distribute load</li>
<li>Cluster Configuration: Deploy Spotfire in a clustered environment to ensure high availability and failover</li>
<li>Session Pooling: Optimize session pooling to handle more users by reusing Web Player sessions efficiently.</li>
<li>Resource : Set resource quotas to prevent a single user or dashboard from consuming excessive resources</li>


```python

```
