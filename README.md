# Software Development (Python) 

**Annabelle Kiefer (s1111172)**  

## A2: Conda Environments

### Overview 

In this assignment, two different yml-files were used to recreate environments with conda.  
The files were acquired by forking the following repo (https://github.com/augustinh22/geo-software-dev/tree/main).

1. `software_dev_v1.yml`
2. `software_dev_v2.yml`  

This assignment was carried out using the commandline (**Anaconda PowerShell Prompt**).

### Process
#### 1. Cloning the Repository

The repository was cloned using the following command in the Anaconda Prompt:

```bash
git clone https://github.com/augustinh22/geo-software-dev.git 
cd geo-software-dev
cd A2
dir
```
#### 2. Recreating the first Environment

The first environment was recreated using the following command in the Anaconda Prompt:

```bash  
conda env create -f software_dev_v1.yml  
conda activate software_dev_v1
conda list
conda deactivate
```
**Screenshots**

![image](https://github.com/user-attachments/assets/29d72219-8aca-4b05-94ca-80633b23fd12)

*No errror messages occured while recreating this environment.*

#### 3. Recreating the second Environment

The second environment was recreated using the following command in the Anaconda Prompt:

```bash  
conda env create -f software_dev_v2.yml  
conda activate software_dev_v2
conda list
```
**Screenshots**

![image](https://github.com/user-attachments/assets/339868d8-42df-4dd9-9e7d-4302b7d5162b)

*No errror messages occured while recreating this environment.*

#### 4. Anaconda Navigator

![image](https://github.com/user-attachments/assets/5bf83ef7-944f-4da3-8e6a-ec0fa70f7107)

*The created environments are now also visible in the Anaconda Navigator.*











