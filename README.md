\# Account Management Brief: Nova Markets (NOVA-FX) Escalation



\## What's going on

Nova Markets' reported dashboard approval rate drop from 79.62% (Apr–May) to 72.39% in June is primarily driven by business expansion rather than system failure. The decline is explained by three factors:



\* New Corridor Launch (NBLX-07): On June 2, local bank transfer route `NBLX-07` went live for IDR (Indonesia) and VND (Vietnam). Tighter risk rules applied on June 8 resulted in a lower processor approval rate (\~40.6%). Processing 2,881 attempts in June (28% of total volume), this new corridor pulled down the overall aggregate average.

\* Japanese Card BIN Changes (SORVA-14): On June 11, acquirer BIN reallocations caused JPY card approval rates on route `SORVA-14` to drop from 70.16% to 61.16%.

\* Portal Exclusion Distortion: The merchant dashboard excludes risk-filtered attempts. Pre-routing risk blocks on `NBLX-07` (655 attempts) distorted the ratio shown on their portal.



Financial Reality: Nova Markets did not lose revenue on established routes. The launch of IDR/VND bank transfers brought in \*\*$355,593 USD\*\* in net new, approved deposit volume.



\## What we should do

\* Merchant Explanation: Clarify that the lower overall percentage stems from entering new Southeast Asian markets (IDR/VND) with strict risk controls, which successfully generated over $355K USD in net-new converted deposits.

\* Internal Action Items:

&#x20; 1. Reroute JPY card traffic from `SORVA-14` to `KRTX-03` (which maintains an 82.11% approval rate).

&#x20; 2. Optimize pre-routing risk screening parameters on `NBLX-07` to reduce unnecessary declines.

&#x20; 3. Update portal documentation to clarify how risk-filtered attempts affect visible metrics.



\## Assumptions and open questions

\* \*Assumptions: 

&#x20; \* Excluded June 29–30 attempts as incomplete, following the operations log extract cutoff window.

&#x20; \* Computed portal metrics using the merchant local timezone (UTC+8) and deposit attempts (`order\_type == 'SALE'`).

\* Open Questions:

&#x20; \* What are the target chargeback and risk thresholds for IDR and VND traffic?

&#x20; \* Can commercial teams provide expected baseline conversion rates prior to launching new corridors?



\## How to reproduce

1\. Ensure Python 3.9+ and `pandas` are installed (`pip install pandas`).

2\. Place raw CSV files (`orders.csv`, `routes.json`, etc.) in the `data/` subdirectory.

3\. Run the script:

&#x20;  ```bash

&#x20;  python analysis.py

