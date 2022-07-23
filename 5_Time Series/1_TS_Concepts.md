<h1 style='color:darkcyan;text-decoration:underline'>Concepts</h1>

<div style='width:1000px;margin:auto'>

<details><summary>Types of <b>Termporal</b> Data</summary>
<ul>Temporal data can contain information about the following:
<li><b>Events:</b> An event is a change in the state of an object at a given time. Event = Time + Object State.<br> Examples of events are posting a tweet, sending an email, or sending a message.
</li>
<li> <b>Measurements:</b> Measurements records values across time. Measurement = Time + Measures.<br> Examples of measurements are sensor data, revenue, and stock values.</li></ul>

<ul>Another view of time can be based on how it progresses:
<li><b>Sequential:</b> We consider time as continuous linear values here. An example of this
type is a Unix timestamp.</li>
<li> <b>Cyclical:</b>  Time can be viewed as a recurrent event, where it is understood as fixed periods, such as weeks or months. The cyclical interpretation of time is used to compare values for the same period, such as sales values per month or yearly temperature change.</li>
<li><b>Hierarchical:</b> Another way to understand temporal information is through an hierarchical pattern. A hierarchical time structure helps us to visualize data at different levels. Suppose you are plotting sales data for each month. To understand the pattern for each week for a given month, we are hierarchically breaking the time from a larger periods (months) into smaller periods (weeks).</li></ul>


</details>
<details><summary><b>Temporal</b> Data vs <b>Time-Series</b> Data</summary><br>
- <b>Time-Series</b> Data: is a more refined version of temporal data where observations are taken at equally spaced points in time successively.<br>
- <b>Temporal</b> Data: contains observations that simply attached to time, and the intervals may not be equally spaced.
</details>


</div>