# Research: environment-variable drift

AI-assisted coding raises verification work: 75% of developers report greater
responsibility for validating AI output ([Atlassian 2026](https://d3bdzitctqoj2j.cloudfront.net/teams/software-development/state-of-developer-experience-2026)).
**EnvFence** is a free local receipt for environment variables referenced in
source but absent from `.env.example`, and documented variables no longer
referenced. It uses only Python text scanning; it never reads `.env`, executes
code, or uploads data.
