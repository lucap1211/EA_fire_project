[![DOI](https://zenodo.org/badge/798408877.svg)](https://zenodo.org/doi/10.5281/zenodo.12574886)

# Earth Analytics Final Project
## 2024 Summer

## Project Overview
For my final project I am interested in exploring the narrative text fields of the ICS-209-PLUS-WILDFIRE dataset. The ICS-209-PLUS-WILDFIRES is a fire-focused subset of the [all-hazards dataset](https://www.nature.com/articles/s41597-023-01955-0) mined from the US National Incident Management System 1999–2020 by St. Denis et al. (2023).  I will process the narrative fields to convert text about societal impacts into a suitable format for natural language processing and analyze text to find links between fire hazard characteristics, incident response, and societal impacts/threats incrementally across all phases of active response. My main question that drives the anaysis is:

How can we connect societal impacts and geophysical metrics by topic modeling methods on incidence reporting's narrative fields?


## Installation
The project will run in an updated [earth-analytics-python-env](https://github.com/earthlab/earth-analytics-python-env). The additional library neccessary for the text processing steps is **[spaCY](https://spacy.io/usage), that is included in the updated environmnet.yml file in this repository.

## How to run the analysis
The project followed guidelines for creating reproducible workflows. The [main notebook (dixie_caldor_text_analysis.ipynb)](dixie_caldor_text_analysis.ipynb) runs the text analysis. This workflow can run without previously running the [data processing notebook](ICS-209-PLUS-WILDFIRE_data_processing.ipynb) since the neccessary sample code is avaialble [here](data/processed/dixie-caldor-threat.csv).

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

## Analysis

![Project Workflow](https://github.com/lucap1211/EA_fire_project/blob/main/graphics/workflowwhite.png)

## Results

By leveraging Named Entity Recognition (NER) and other natural language processing techniques, we can extract valuable information from ICS-209 narrative fields. This analysis helps link geophysical fire metrics with societal impacts, providing a deeper understanding of how wildfires affect communities.
See the 'Final blog post' files in Blog Posts folder for a detailed summart on findings illustrated by graphs and visuals from the analyses.

## Conclusion

Narrative reporting from ICS-209 forms offers invaluable, previously non-synthesized insights into the societal impacts of large wildfires. By analyzing these narratives with advanced natural language processing techniques like Named Entity Recognition (NER), we can better understand the intricate connections between fire hazard characteristics, management actions, and their societal effects. The case studies of the Dixie and Caldor fires demonstrate the potential of this approach to inform and improve wildfire management.

Moving forward, I plan to enhance the accuracy of named entity recognition by fine-tuning models and creating customized pipelines. Additionally, building metadata to categorize threats by type will further refine our ability to link narrative data with other critical wildfire metrics, paving the way for more informed and effective fire management strategies.

## Contributors
This project will be mentored by [Lise Ann St. Denis](https://earthlab.colorado.edu/our-team/lise-ann-st-denis).


## Sources

-   St. Denis, L.A., Short, K.C., McConnell, K. et al. All-hazards dataset mined from the US National Incident Management System 1999–2020. Sci Data 10, 112 (2023). [DOI](https://doi.org/10.1038/s41597-023-01955-0)

