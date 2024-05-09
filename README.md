# Earth Analytics Final Project
## 2024 Summer

## Project Overview
For my final project I am interested in exploring the narrative text fields of the ICS-209-PLUS-WILDFIRE dataset. The ICS-209-PLUS-WILDFIRES is a fire-focused subset of the [all-hazards dataset](https://www.nature.com/articles/s41597-023-01955-0) mined from the US National Incident Management System 1999–2020 by St. Denis et al. (2023).  I will process the narrative fields to convert text about societal impacts into a suitable format for natural language processing and analyze text to find links between fire hazard characteristics, incident response, and societal impacts/threats incrementally across all phases of active response. My main question that drives the anaysis is:

How can we connect societal impacts and geophysical metrics by topic modeling methods on incidence reporting's narrative fields?


## Installation
The project will run in the public [earth-analytics-python-env](https://github.com/earthlab/earth-analytics-python-env) that contains the dependencies and libraries needed for the project. If other libraries becomes neccessary for the project, they will be listed here as additional requirements. 

## Data
For my project, I plan to heavily focus on text-based narrative data (ICS-209-PLUS-WILDFIRES) and use geospatial data (like Monitoring Trends in Burn Severity).

### ICS-209-PLUS-WILDFIRES

- Standardized, on-scene Incident Status Summary
- Part of the National Incident Management System (NIMS)
- Text-based narrative wealth of data
- Science-grade situation reports focusing on large wildfires
- Daily “informational snapshots” of fire response/management
- View into the decision-making process
    - Large fire event development and response

### Monitoring Trends in Burn Severity

The Monitoring Trends in Burn Severity (MTBS) dataset is a comprehensive dataset that maps the fire severity and perimeters of large wildfires in the United States across all ownerships. The MTBS vector datasets include burn scar boundaries that are delineated from satellite imagery and burn severity index data at a map scale of 1:24,000 to 1:50,000. I will primarily use the vector burn area boundaries.


## Analysis

![Project Workflow](https://github.com/lucap1211/EA_fire_project/blob/main/graphics/workflowbackground.png)

## Results
Later

## Conclusion
Later

## Contributors
This project will be mentored by [Lise Ann St. Denis](https://earthlab.colorado.edu/our-team/lise-ann-st-denis).


## Sources
-   Eidenshink, J., Schwind, B., Brewer, K., Zhu, Z.L., Quayle, B. and Howard, S., 2007. A project for monitoring trends in burn severity. Fire ecology, 3, pp.3-21. 

-   St. Denis, L.A., Short, K.C., McConnell, K. et al. All-hazards dataset mined from the US National Incident Management System 1999–2020. Sci Data 10, 112 (2023). [DOI](https://doi.org/10.1038/s41597-023-01955-0)

