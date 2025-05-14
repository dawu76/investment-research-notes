### RW Pro onboarding notes

---

Highlights
- RW Pro API key: use API to pull weights into spreadsheet or some other application
- Research pods to house clean data and libraries for cleaning and analyzing data: use Google Colab notebooks to share code snippets of common code patterns / queries
- What's in the "Lab"? Edge database: maintained in Github, in the form of a spreadsheet or Kanban board, that collects info about the edges that RW has investigated before. On main page, click on Lab > Lab HQ > Course Content with videos
- Macro Pod: organized in similar way, with research findings and scripts, and links to any datasets; click on one of the research notebooks to see a walk-through of the findings and code; the notebook will pull code from APIs or from files in Github; occasionally, there may be changes in Colab or libraries that cause the code to break - if that happens, ask for help on Discord.
- There's a RwTools script with common utility snippets for downloading data via API, calculating certain quantities like EWMA, creating a histogram of returns, etc. This script is sourced at the top of many of these notebooks.
- In Colab, go to the settings cog and authorize it to have access to Github; also check the option to access private repos. Also go to Site settings and paste the URL of a Colab notebook into 'Custom snippet notebook URL' field, where the URL is copied from the Lab HQ course > 'Colab: Reproducible Research in the Lab' section. These same instructions are also in that course module. By doing so, you can get easy access to useful research code snippets from any notebook by clicking on '<>' in the LHS menu and filtering in the window. The research code snippets notebook itself is organized by research pod - e.g. equity factors (EF), macro, crypto, etc.
