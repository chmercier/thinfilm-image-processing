# XRD Processing & Subtraction Overview

This project connects image preprocessing, cropping, and data subtraction into one workflow for working with XRD data.

## What each file does

### Hackternoon.py
Handles image preprocessing.  
Loads a TIFF image, saves rotated and recolored versions, and can split the image into quadrants. Useful for visually exploring scattering patterns and preparing images for later steps.

### CenterCrop.ipynb
Interactive notebook for experimenting with center cropping.  
Helps you choose and refine the region of interest before moving forward with analysis.

### Center_crop_tutorial.ipynb
Walkthrough notebook showing how center cropping works and how to apply it.  
Great as a reference when learning or onboarding someone new.

### classes.py
Defines the background-subtraction logic.  
Contains the `Subtract_Save` class, which reads text-based scattering files, subtracts a substrate curve from a total signal curve, and prepares the cleaned data for saving.

### Sub_With_Classes.py
Example script that uses `Subtract_Save`.  
Runs the subtraction, then plots the total signal, substrate, and subtracted result so you can compare them visually.

## How they fit together

Images are first cleaned and explored in Hackternoon.  
Relevant regions are cropped using the center-crop notebooks.  
Integrated text files from those images are passed into the subtraction tools in `classes.py`, and `Sub_With_Classes.py` visualizes the final background-corrected result.
