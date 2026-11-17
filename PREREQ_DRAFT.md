# Detecting Phishing Websites Under a False-Alarm Budget

**Group members:** [Name 1], [Name 2], [Name 3]
**Course:** DS 4021, [Submission date]

---

### Motivation

Phishing websites imitate trusted pages, such as bank logins or package-delivery notices, to trick people into handing over passwords and payment details. Phishing is one of the most common forms of cybercrime: [ADD ONE STAT, e.g. phishing/spoofing was the most-reported complaint type in the FBI's 2024 Internet Crime Report [3], or the number of attacks in the latest APWG trends report [4]]. Blocklists only catch sites that have already been reported, so researchers train machine-learning classifiers on features of a site's URL, page source, and domain history, such as whether the site uses a valid SSL certificate, whether the address is a raw IP, and how old the domain is [1], [2], [5]. Most studies report overall accuracy, but in practice a detector has two kinds of error with very different costs. Flagging a legitimate site is an annoyance that leads users to ignore warnings, while missing a phishing site can expose someone to fraud. Deployed filters therefore have to hold false alarms to a small, fixed rate, and the useful question becomes how many phishing sites a model still catches at that rate. Comparing models at a fixed false-positive rate, and asking whether a small, interpretable set of features comes close to the full set, shows which approach is most practical when false alarms are capped.

### Research Question

At a fixed false-positive rate (e.g., 1%), which classifier (a support vector machine, a random forest, or a neural network) detects the largest share of phishing websites, and how much of that detection rate is kept with a small, interpretable subset of features?

### Dataset Description

We use the *Phishing Websites* dataset from the UCI Machine Learning Repository [1] (https://archive.ics.uci.edu/dataset/327/phishing+websites), compiled by Mohammad, Thabtah, and McCluskey from PhishTank, MillerSmiles, and Google search results [2]. The original file has 11,055 websites and 30 categorical features plus a binary label (phishing or legitimate). The features cover the URL (e.g., IP address in the URL, URL length, "@" symbol), the page's HTML and JavaScript (e.g., pop-up windows, form handlers), and the domain (e.g., domain age, DNS record, web traffic). Twenty-two features are binary and eight are ternary (legitimate / suspicious / phishing). There are no missing values, but 5,206 rows are exact duplicates. We removed them before splitting, which leaves 5,849 unique websites, of which 51.6% are phishing and 48.4% are legitimate. The features separate the classes clearly. For example, 90.4% of legitimate sites have a trusted SSL certificate, compared with 14.6% of phishing sites. We set aside a stratified 20% reporting set (1,170 sites) that will not be used until the final evaluation. The remaining 4,679 sites form the development set.

### GitHub Repository

https://github.com/[username]/[repo-name]

### References

[1] R. M. Mohammad, F. Thabtah, and L. McCluskey, "Phishing Websites," UCI Machine Learning Repository, 2015. [Online]. Available: https://doi.org/10.24432/C51W2X

[2] R. M. Mohammad, F. Thabtah, and L. McCluskey, "Predicting phishing websites based on self-structuring neural network," *Neural Comput. Appl.*, vol. 25, no. 2, pp. 443–458, 2014.

[3] Federal Bureau of Investigation, "Internet Crime Report 2024," Internet Crime Complaint Center (IC3), Washington, DC, USA, 2025.

[4] Anti-Phishing Working Group, "Phishing Activity Trends Report, [quarter] [year]," APWG, [year].

[5] O. K. Sahingoz, E. Buber, O. Demir, and B. Diri, "Machine learning based phishing detection from URLs," *Expert Syst. Appl.*, vol. 117, pp. 345–357, 2019.
