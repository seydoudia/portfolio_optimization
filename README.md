# portfolio_optimization

Building S&P500 portfolios with and without carbon footprint penalization. 

In this project, we analyze different asset management strategies as well as KPIs to compare them. The project simulates investment strategies througout a duration of 20 year with the following models : 
- EW : equally weighted
- GMW : global minimum variance
- MAXDECOR : max decorrelation
- MAXDIV : max diversification
- MSR : maximum sharp ratio

Each strategy optimizes the weights on 2 years of training data and performs the validation on the following three months. The rolling window is also of three months which makes a total of 78 different optimizations throughout the entire simulation for each strategy. 
The assets are initially selected by taking into account the 5 best assets with the lowest carbon footprint from each of the 10 sectors of the S&P500.Thus, each portfolio has the same 50 assets. 
Then, for each optimization strategy, the objective functions are penalized by each asset's carbon footprint. The result are then analyzed. 

The KPIs computed are : 

- Return
- Volatility
- Information Ratio
- Diversification Index
- Sharp Ratio
- Tracking Error
- Excess Return
- Diversification Index

The entire project was developed from scratch and conducted in French The report notebook can be found in the code folder under the name of [RAPPORT_DIA_MILADINOVA_PROJET_FINANCE.ipynb](https://github.com/seydoudia/portfolio_optimization/blob/main/CODE/RAPPORT_DIA_MILADINOVA_PROJET_FINANCE.ipynb)
This project was conducted during the Msc. in Energy Systems Optimization of Mines Paris in collaboration with [Ms. Simona MILADINOVA](https://www.linkedin.com/in/simona-miladinova-839b8a17a/) and [Mr. Seydou DIA](https://seydoudia.github.io/Data-Science-portfolio/) under the supervising of [Mr. MARTELLINI](https://www.edhec.edu/fr/corps-professoral-et-chercheurs/martellini-lionel-phd), Head of  EDHEC Risk-Institute, as part of the Sustainable Finance course. 

If the reader wishes to dig further into the project other data can be found in the CODE folder

- asset_optimization : notebook that optimizes the weights for each strategies with and without carbon penalization.
- computing_metrics.ipynb : notebook that anlyses results of optimization without penalization
- computing_metrics_carbon_penalty : notebook that anlyses results of optimization with penalization
- proc_data : notebook to process raw data of carbon footprint, S&P500 and perform preselection of weights

For the results tables, they can be found in the PROC_DATA folder : 

- The weight csv files represent the weights calculated for each strategies with and without carbon penalization.
- The optimize assets csv files represent the assets optimzed calculated for each strategies 
- The dic_metrics and dic2use file represent the metrics computed with and without carbon penalization.


For more projects on Data Science, Energy and Sustainability, follow this [link](https://seydoudia.github.io/Data-Science-portfolio/)
