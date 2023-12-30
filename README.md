# Dynamic Audio Implementation With Ren'Py

Slides for AlfredPros' talk in VNConf 2024. This slide is made using Ranim template.

## Usage

it is advised to run this project in between version `7.4.6` to `7.5.1`/`8.0.1`.

Here are the reasons why:
- Since this project contains matrixcolor ATL and camera statement, you should run this on Ren'Py `7.4.6` or above.
- Due to the newer focus displayable behavior change in Ren'Py `7.5.2`/`8.0.2`, it is not optimal when you use button interactions in timer-based screen. However, in the newer version (I tried version `7.6.3`/`8.1.3`), this issue has been fixed.
- In Ren'Py version `7.6`/`8.1`, audio fadein/fadeout behavior has changed which makes seamless transition between channels for crossfade more awkward to do.

## About Ranim

A manim-inspired Ren'Py template for presentation and animation. Ranim is a personal project I made while making this VNConf 2024 slides project. 
The project is still unreleased as of right now.
However, you are free to use the current version of Ranim from what I had in this project.

Core files : `definitions.rpy` (customizable and utility screens), `images/util` (images used for utility screens)
