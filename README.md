The goal of this project is for Zach to demonstrate familiarity and skill with handling data from a multitude of aspects, from raw, uncleaned data, to polished data, to insights, predictive models, and more, demonstrating data engineering abilities with Docker and database design along the way.

![McQueen Kachow, remote](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXJmZTdrZ2k5dGwxY284bzhpNWJ0M3prMjhlenUya2pkcmlnZHd2bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/B1CrvUCoMxhy8/giphy.gif)

What is this project?

As an individual who often finds himself doing research into a varity of topics in his spare time, especially in the automotive industry, I wanted to showcase my skills in data science by engineering solutions that empower people to analyze automotive data from a dataset that I have amassed with a custom web scraper. My dream is for whenever I have a question about a particular model of car, I can use a dashboard I have pre-designed that contrasts this car against other models, potentially against entire industry and market trends.

Why am I doing this?

As a current job-seeker within the realm of data science, I have decided that one needs more in today's economy than simple projects that demonstrate simple capabilies, such as data engineering, cleaning, evaluation and analysis, predictive model creation, Docker and database familiarity, and other skills pertaining to data science and engineering. To just do one or two of these would be to compromise.

If I don't have a job by the end of this project, it will showcase ALL of these skills. I don't know what will help if this won't.

NOTE FOR NOVEMBER 1: This scraper no longer seems to run, since the website it scrapes seems to have changed in design. Shucks.

![Computer Destruction, remote](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmg0cTZob2F3bzdwemZreXBrdXY4b3A2dmozMjNndXUxcGhicXZ5dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ohs81rDuEz9ioJzAA/giphy.gif)

However, I still consider the dataset I have amassed respectable in size, so I will implement several data science projects linked below. After these are implemented, I will re-engineer a superior scraper that will demonstrate capabilities in database design and Docker implementation. 
But for now...

WHAT IS SCRAPED?
- All cars listed within a 100-mile radius of each city in the filters-json file is scraped.
- Each record from each car contains the following data points:
  - Make/Year
  - Model, often with trim details
  - Listed price
  - Rated assessment of the price (e.g. good deal/bad deal, scraped directly from the website)
  - Mileage
 
Here's some links to what I've completed so far with the rest of the project:

[My first data app!](https://deepnote.com/app/portfolio-1e78/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=data-app&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)

[And its corresponding notebook](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/Data-Mining-1-Single-Model-Dash-28562771e0f44983bd9d7855132e2914?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)

Python Data Cleaning Scripts:
  - [Data Cleaning 1](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/PROTOTYPING-Cleaning-Part-1-Basic-Fixes-c3b51950207c45ed9eed74fda8b100a8?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)
  - [Data Cleaning 2](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/PROTOTYPING-Cleaning-Part-2-Data-Consolidation-339f98ad8c8b4df8adbc1ffab6252423?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)
  - [Data Cleaning 3](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/PROTOTYPING-Cleaning-Part-3-Duplicate-Deletion-26b632f0cd1244bebf000140a621d81f?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)
  - [Data Cleaning 4](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/PROTOTYPING-Cleaning-Part-4-Basic-Tokenization-8e9f92cf5797412a83232838dc22d9e4?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)
  - [Data Cleaning 5](https://deepnote.com/workspace/Portfolio-c507df57-5746-4fcd-817d-ab2e0f30ee5a/project/AutoAnalysis-ae8caaae-2fe4-45ea-b02c-a9a75784008a/notebook/PROTOTYPING-Cleaning-Part-5-Adaptive-JSON-Dash-v1-2a19f7ccb4d14b12938a0301155788f1?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=ae8caaae-2fe4-45ea-b02c-a9a75784008a)
