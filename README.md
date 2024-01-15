## Setup Guide for Distributed Analysis Systems

This tutorial describes how to build up an Ansible-based distributed analysis system for proteome analysis. 
Cloning the repository, setting up the required SSH keys, setting up the control node, and starting the analytic pipeline are all part of the setup procedure.

## Link to the Control Node in Step 1

Ensure that the lecturer key was used while building the cluster. After that, run the following command: 
```bash

ssh -i path/to/key ec2-user@ec2-35-178-42-199.eu-west-2.compute.amazonaws.com
```

## Step 2: Transfer the control node's private lecturer key.
In order for the control node to access the workers, this is necessary.

```bash
scp path/to/lecturer_key ec2-user@ec2-35-178-42-199.eu-west-2.compute.amazonaws.com:~/.ssh/lecturer_key
```
## Step 3: Set up the control node with the necessary packages.
This sets up the control node with Python, Pip, Git, and Ansible installed.

```bash
sudo yum update -y

sudo yum install -y python3 git

sudo yum install -y python3-pip

sudo pip3 install ansible

sudo pip3 install pandas
```

## Step4: Clone the github repository for the coursework
Use the following command to clone the repository and install the necessary code on the control node:
```bash

git clone https://github.com/Dennoh12
```

## Execute the pipeline in Step 5
Place the ids you wish to analyze in the experiment_ids.txt file before starting the workflow.

Use this command to launch the distributed analysis:
```bash
cd cw0235
ansible-playbook --private-key=~/.ssh/lecturer_key -i hosts Biochemistry_Pipeline
```


## Step 6: Obtain outcomes
Following pipeline completion, the following files in the cw0235 directory will contain the results:

- best_hits.csv
- stats.csv

