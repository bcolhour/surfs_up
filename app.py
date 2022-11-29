{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e3063b21-3bf5-4fe0-bdd5-7b2445cf034d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the Flask dependency\n",
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "035d53df-5929-4670-b2b5-bb094492aad8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#  create a new Flask app instance\n",
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "43312315-61c6-4394-ac50-fed74a6a74f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# define the starting point, also known as the root. \n",
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello world'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfd37cd7-453c-4fce-ad97-0ddc3d823e53",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
