# portfolio_optimization

Building S&P500 portfolios with and without carbon footprint penalization. 

In this project, we analyze different asset management strategies as well as KPI to compare them. The project simulates investment strategies througout a duration of 20 year with the following strategies : 
- EW
- GMW
- MAXDECOR
- MAXDIV
- MSR

Each stragy optimizes the weights on 2 years of training data and performs the validation on the following three months. The rolling window is also of three month which makes a total of 78 different optimization throughout the entire simulation for each strategy. 
The assets are initially selected by taking into account the 5 best assets from each sector for a portfolio of 50 assets. Then, for each optimization strategy, the opbjective functions are penalized by each asset's carbon footprint. The result are then analyzed. 

The entire project was conducted in French and the report notebook can be found in the code folder under the name of RAPPORT_DIA_MILADINOVA_PROJET_FINANCE.ipynb 
This project was conducted during the Msc. in Energy Systems Optimization of Mines Paris in collaboration with [Ms. Simona MILADINOVA](https://www.linkedin.com/in/simona-miladinova-839b8a17a/) and  the supervising of [Mr. MARTELLINI](https://www.edhec.edu/fr/corps-professoral-et-chercheurs/martellini-lionel-phd), Head of  EDHEC Risk-Institute, as part of the Sustainable Finance course. 

If the reader wishes to dig further into the project other data can be found in the CODE folder

- asset_optimization : notebook that optimizes the weights for each strategies with and without carbon penalization.
- computing_metrics.ipynb : notebook that anlyses results of optimization without penalization
- computing_metrics_carbon_penalty : notebook that anlyses results of optimization with penalization
- proc_data : notebook to process raw data of carbon footprint, S&P500 and perform preselection of weights

For the results tables, they can be found in the PROC_DATA folder : 

- The weight csv files represent the weights calculated for each strategies with and without carbon penalization.
- The optimize assets csv files represent the assets optimzed calculated for each strategies 
- The dic_metrics and dic2use file represent the metrics computed with and without carbon penalization.

