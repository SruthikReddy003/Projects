
# Drug Induced CardioToxicity Analysis Using Graph Neural Networks

Cardiotoxicity refers to the deleterious results of drug use on the cardiovascular system, specifically the heart muscle and blood vessels. The impact of various cardiovascular diseases can be increased by using some prescription drugs and illicit drugs. Some examples are drugs that are used to extend the QT interval of the heart, anti-cancer drugs like anthracyclines and some general anti-inflammatory drugs.

Graph Neural Networks(GNNs) learn to extract various features from graphs by collecting information from nodes and edges. These Neural networks can be used to perform various tasks such as node property prediction, link prediction, node classification, and graph classification.

Drug candidates typically inhibit the potassium-ions channel that regulates the human ether-a-go-go-related gene (hERG), a protein connected to heart beat rhythm. Long QT syndrome, a serious cardiac adverse effect that poses a serious risk of death, is caused by the obstruction. The ability to foresee medication-induced hERG-related cardiotoxicity may speed up drug discovery by eliminating risky drug candidates. More than 9000 compounds with hERG activity are covered by the drug cardiotoxicity dataset.Four subsets of the data are used: train, test-iid, test-ood1, and test-ood2.Each molecule in the collection has 2D graph labels to help with graph neural network modelling. The molecules' atoms are its nodes, and its bonds are its edges. The basic characteristics of each atom, such as its kind, are encoded in a vector that represents each atom. Bonds follow a similar reasoning. 

The dataset can be found [here](https://www.tensorflow.org/datasets/catalog/cardiotox).
