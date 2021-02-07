# Postmortem Report 
## Date: 
2021-02-06

## Authors:
Ons Jannet

## Status:
Complete, action items in progress

## Impact:
Estimated 1.13B queries lost, no revenue impact

## Issue Summary
A backend failure due to high load accured between 02/04 7:55 PT and 02/04 9:00 PT. Due to a high demand on a certain concert and after the artist tweeting about it an exceptionally traffic rushed to our website that caused the backend failure.


## Timeline
* 02/04 7:55 PT - Camila Cabello's Posted about new tour Dates, sharing a link to Ticketsales
* 02/04 7:57 PT - Traffic to Ticketsales increased by 130x
* 02/04 7:58 PT - Under Load, backends started melting down
* 02/04 8:00 PT - All traffic to Ticketsales is failing
* 02/04 8:05 PT - a try to reinstate load balancing across all clusters for 1% traffic
* 02/04 8:07 PT - balancing 10% of traffic across nonsacrificial clusters
* 02/04 8:12 PT - balancing 30% of traffic across nonsacrificial clusters
* 02/04 8:17 PT - balancing 50% of traffic across nonsacrificial clusters
* 02/05 8:30 PT - Outage ends, all the traffic being balanced across all clusters
* 02/05 9:00 PT - Incident ends, reaching 30 minutes nominal performance exit citerion

## Root Cause
Cascading failure due to exceptionally high load. Clients rushed to get front seats causing latent bug triggered the sudden increase in traffic. Under normal circumstances, the rate of task failures due to high traffic is low enough to be unnoticed.

## Preventative Measures
Directing traffic to sacrificial cluster and adding 10x the capacity to mitigate the cascading failure. Updating index deployed, resolving interaction with latent bug.

## Supporting information
No supporting information at this time
