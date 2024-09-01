{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "249dacc9",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.292063Z",
     "iopub.status.busy": "2024-09-01T08:20:02.291579Z",
     "iopub.status.idle": "2024-09-01T08:20:02.765184Z",
     "shell.execute_reply": "2024-09-01T08:20:02.763633Z"
    },
    "papermill": {
     "duration": 0.484725,
     "end_time": "2024-09-01T08:20:02.768207",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.283482",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b8eac34",
   "metadata": {
    "papermill": {
     "duration": 0.005513,
     "end_time": "2024-09-01T08:20:02.779776",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.774263",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Block A:\n",
    "- (funktion, argument, return)Print, datatyper & variabler, operatorer\n",
    "- F-string, string methods, If, elif, else\n",
    "- Listor, indexing & slicing, \n",
    "\n",
    "Block B:\n",
    "- Funktioner, parametrar/argument, recursion\n",
    "- Range, for, while loop, continue & break\n",
    "- Dict(case match), set, tuples\n",
    "\n",
    "Block C:\n",
    "- list comprehension\n",
    "- Filhantering, csv, json\n",
    "- Try,except\n",
    "- Streamlit\n",
    "\n",
    "Block D:\n",
    "- Matplotlib & pandas\n",
    "\n",
    "Block E:\n",
    "\n",
    "- Miniräknare\n",
    "- API\n",
    "- Pokedex\n",
    "- Deploy App\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ac40318",
   "metadata": {
    "papermill": {
     "duration": 0.005778,
     "end_time": "2024-09-01T08:20:02.791227",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.785449",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Övning 1**1/9**\n",
    "\n",
    "#### Calculator\n",
    "\n",
    "# #1\n",
    "\n",
    "Objective: Write a program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. \n",
    "\n",
    "Instructions:\n",
    "\n",
    "- Create a function for each of the following operations: addition, subtraction, multiplication, and division.  \n",
    "- Each function should take two arguments (the numbers to operate on) and return the result.  \n",
    "- Test the functions by calling them with sample inputs and printing the results."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bce0f7bf",
   "metadata": {
    "papermill": {
     "duration": 0.005889,
     "end_time": "2024-09-01T08:20:02.803416",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.797527",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# #2\n",
    "\n",
    "Objective: Extend the calculator to allow the user to choose an operation and input the numbers.\n",
    "\n",
    "Instructions:\n",
    "\n",
    "Prompt the user to select an operation (addition, subtraction, multiplication, or division).  \n",
    "Ask the user to input two numbers.  \n",
    "Use the functions from Exercise 1 to perform the selected operation on the input numbers.  \n",
    "Print the result."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4e6b15e",
   "metadata": {
    "papermill": {
     "duration": 0.005472,
     "end_time": "2024-09-01T08:20:02.814830",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.809358",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# #3\n",
    "\n",
    "Objective: Improve the calculator by adding a loop to allow multiple calculations and enhance error handling.\n",
    "\n",
    "Instructions:\n",
    "\n",
    "- Use a loop to allow the user to perform multiple calculations without restarting the program.  \n",
    "- Add error handling to manage invalid inputs, such as non-numeric inputs or invalid operation choices.  \n",
    "- Provide an option to exit the program.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea3117b2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.828453Z",
     "iopub.status.busy": "2024-09-01T08:20:02.827872Z",
     "iopub.status.idle": "2024-09-01T08:20:02.833302Z",
     "shell.execute_reply": "2024-09-01T08:20:02.832016Z"
    },
    "papermill": {
     "duration": 0.015509,
     "end_time": "2024-09-01T08:20:02.836074",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.820565",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#1 Skriv ett program för att hitta en triangels area\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ee76ed26",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.849462Z",
     "iopub.status.busy": "2024-09-01T08:20:02.849033Z",
     "iopub.status.idle": "2024-09-01T08:20:02.854402Z",
     "shell.execute_reply": "2024-09-01T08:20:02.853165Z"
    },
    "papermill": {
     "duration": 0.015186,
     "end_time": "2024-09-01T08:20:02.857063",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.841877",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Skriv ett program som swapar två variabler\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6b221cee",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.870335Z",
     "iopub.status.busy": "2024-09-01T08:20:02.869894Z",
     "iopub.status.idle": "2024-09-01T08:20:02.875353Z",
     "shell.execute_reply": "2024-09-01T08:20:02.874176Z"
    },
    "papermill": {
     "duration": 0.015092,
     "end_time": "2024-09-01T08:20:02.877989",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.862897",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#2 Skriv ett program som genererar random siffror\n",
    "\n",
    "#hint: importera bibliotek\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "50319183",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.891742Z",
     "iopub.status.busy": "2024-09-01T08:20:02.891313Z",
     "iopub.status.idle": "2024-09-01T08:20:02.896838Z",
     "shell.execute_reply": "2024-09-01T08:20:02.895515Z"
    },
    "papermill": {
     "duration": 0.015216,
     "end_time": "2024-09-01T08:20:02.899319",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.884103",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#3 Skriv ett program som omvandlar kilometer till usa mil.\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b1a3b66f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.912663Z",
     "iopub.status.busy": "2024-09-01T08:20:02.912227Z",
     "iopub.status.idle": "2024-09-01T08:20:02.917391Z",
     "shell.execute_reply": "2024-09-01T08:20:02.916166Z"
    },
    "papermill": {
     "duration": 0.014666,
     "end_time": "2024-09-01T08:20:02.919847",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.905181",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#4 Skriv ett program som displayar kalender\n",
    "\n",
    "# tips: importera bibliotek\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "72f2aac9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.933884Z",
     "iopub.status.busy": "2024-09-01T08:20:02.932792Z",
     "iopub.status.idle": "2024-09-01T08:20:02.938410Z",
     "shell.execute_reply": "2024-09-01T08:20:02.937129Z"
    },
    "papermill": {
     "duration": 0.015321,
     "end_time": "2024-09-01T08:20:02.940850",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.925529",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#5 Skriv ett program för att lösa andragradsekvationer\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "60a810af",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.954553Z",
     "iopub.status.busy": "2024-09-01T08:20:02.953988Z",
     "iopub.status.idle": "2024-09-01T08:20:02.959259Z",
     "shell.execute_reply": "2024-09-01T08:20:02.957992Z"
    },
    "papermill": {
     "duration": 0.015297,
     "end_time": "2024-09-01T08:20:02.961990",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.946693",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#6 Skriv ett program som kolla efter skottkår\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6012820e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.976150Z",
     "iopub.status.busy": "2024-09-01T08:20:02.975000Z",
     "iopub.status.idle": "2024-09-01T08:20:02.980525Z",
     "shell.execute_reply": "2024-09-01T08:20:02.979308Z"
    },
    "papermill": {
     "duration": 0.015501,
     "end_time": "2024-09-01T08:20:02.983302",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.967801",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#7 Skriv ett program som printar alla primtal mellan 1-10\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "772895a4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:02.996793Z",
     "iopub.status.busy": "2024-09-01T08:20:02.996081Z",
     "iopub.status.idle": "2024-09-01T08:20:03.001233Z",
     "shell.execute_reply": "2024-09-01T08:20:03.000062Z"
    },
    "papermill": {
     "duration": 0.014815,
     "end_time": "2024-09-01T08:20:03.003844",
     "exception": false,
     "start_time": "2024-09-01T08:20:02.989029",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# 8 Skriv ett program som visar en hel multiplikationstabell\n",
    "\n",
    "#Förslag på output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7ba82f80",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-09-01T08:20:03.017739Z",
     "iopub.status.busy": "2024-09-01T08:20:03.016942Z",
     "iopub.status.idle": "2024-09-01T08:20:03.022101Z",
     "shell.execute_reply": "2024-09-01T08:20:03.020835Z"
    },
    "papermill": {
     "duration": 0.014972,
     "end_time": "2024-09-01T08:20:03.024706",
     "exception": false,
     "start_time": "2024-09-01T08:20:03.009734",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#9 Skriv ett program som printar ut Fibonacci sekvensen\n",
    "\n",
    "#Förslag på output:mn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4190952",
   "metadata": {
    "papermill": {
     "duration": 0.005298,
     "end_time": "2024-09-01T08:20:03.035710",
     "exception": false,
     "start_time": "2024-09-01T08:20:03.030412",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 30761,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 4.695061,
   "end_time": "2024-09-01T08:20:03.563638",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-09-01T08:19:58.868577",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
