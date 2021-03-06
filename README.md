# Towards Robust and Adaptable Diagnosis of Pneumonia from Chest X-ray Data

### Abstract

Chest radiography is a cost effective and powerful investigator method that conveys crucial respiratory information for pneumonia detection. Artificial intelligence (AI) researchers and radiologists have recently reported AI systems that accurately diagnose pneumonia from a chest X-Ray images using deep neural networks when trained on a sufficient large and homogeneous amount of labelled images. However, the robustness and adaptability of these systems, trained minimizing the empirical risk (ERM), remains far way. In fact, ERM have no way of discard environment specific spurious features and take into account confounders, creating an alarming situation in which the systems appear accurate, but fail when tested in new hospitals. We propose here 2 ideas to address this challenge towards a robust and adaptable diagnosis of pneumonia: (i) discard the spurious feature replacing ERM with a robust training routine (i.e. IRM and v-REx); (ii) replace the straight-forward deep neural networks with a new modular architecture, encoding separately the invariant features (in a self-supervised fashion) and the style confounders. Then we validate the impact of each contribution, one at the time, by 2 experiments on real-word data.

#### Project Report: [here](https://github.com/riccardocadei/pneumoniadiagnosis/blob/main/reports/Final%20Report.pdf)


### Team
The project is accomplished by:
- Riccardo Cadei: [@riccardocadei](https://github.com/riccardocadei)
- Raphael Attias: [@raphaelattias](https://github.com/raphaelattias)

### Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── labels         <- Data from third party sources.
    │   └── images         <- Intermediate data that has been transformed.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks with experiments.
    │   ├── dataloader.ipynb  <- Notebook showcase the data environments
    │   ├── model.ipynb       <- Notebook showcase the models
    │   ├── experiment1.ipynb <- First experiment notebook
    │   └── experiment2.ipynb <- Second experiment notebook
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── Final Presentation.pptx 
    │   ├── Final Presentation.mp4 
    │   ├── Final Report.pdf       
    │   ├── Milestone 1.pdf         
    │   ├── Milestone 2.pdf        
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   ├── clean_NIH.py     
        │   ├── dataloaders.py     
        │   ├── datasets.py      
        │   ├── normalize.py  
        │   ├── readdata.py      
        │   └── prepare_env.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── baseline.py      <- Baseline Model from arXiv:2007.10653
        │   ├── chexnet.py       <- SOTA model from arXiv:1711.05225v3
        │   ├── resnet.py        <- SimCLR model from arXiv:2002.05709
        │   ├── style_encoder.py <- Style encoder for experiment 2
        │   ├── super_model.py   <- Model predictor for experiment 2
        │   ├── unet.py          <- Model predictor
        │   ├── evaluate.py      <- Evaluation routine
        │   └── train.py         <- Training routine
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------
