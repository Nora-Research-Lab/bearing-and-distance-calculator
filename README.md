![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Bearing and Distance Calculator
 
*For GIS analysts, surveyors, and field geologists: enter two sets of decimal-degree coordinates to instantly compute the great-circle distance and initial/back bearings between them.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** GIS & Spatial Analysis
 
**Inputs**: The user provides four coordinate values: Point 1 latitude, Point 1 longitude, Point 2 latitude, Point 2 longitude — all in decimal degrees (float, with validation: lat ±90, lon ±180). A dropdown lets the user choose output distance units: kilometers, miles, or nautical miles. A 'Calculate' button triggers the computation.

**Core calculation**: The tool implements the Haversine formula for great-circle distance and the standard bearing formula.

Step 1: Convert all degree values to radians.
Step 2: Compute differences: Δlat = lat2 - lat1, Δlon = lon2 - lon1.
Step 3: Distance via Haversine:
  a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
  c = 2 * atan2(√a, √(1-a))
  d = R * c, where R is Earth radius (6371 km, 3959 miles, 3440 NM) selected per unit.
Step 4: Initial bearing:
  θ = atan2(sin(Δlon)*cos(lat2), cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(Δlon))
  Convert θ from radians to degrees, normalize to 0–360°.
  Back bearing = (bearing + 180) % 360.

**Output**: The tool displays three results: (a) Distance in the selected unit with two decimal places, (b) Initial bearing in degrees (e.g., '45.23°'), (c) Back bearing in degrees. All outputs are read-only text boxes. No plot is generated.

**UI**: Built with Gradio. Layout: two columns — left column for inputs (four number boxes for lat/lon, a dropdown for units, and a button), right column for outputs (three text boxes stacked). The page includes concise instructions and a disclaimer about Earth-spheroid approximations.

**AI component**: None. This is a pure trigonometric calculator.
 
## Run it
 
```bash
docker build -t bearing-and-distance-calculator .
docker run -p 7860:7860 bearing-and-distance-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-30.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
