# Examples using the CrunchtimeOdds API

Site: https://crunchtimeodds.com

Quickstart: `curl -X GET https://crunchtimeodds.com/api/health`

#### Comprehensive odds API serving a blend of sports betting statistics and real-time odds, providing impactful betting resources for users.

The Crunchtime API aggregates consistent and accurate odds data from dozens of bookies and sports leagues to provide real-time odds and powerful statistics in a reliable and accessible manner, all in one convenient place. It features robust request handlers with consistent responses and powerful request routing. It can handle a large number of requests efficiently without sacrificing performance or stability, with fast response times to provide users with a seamless experience.

[Create an account](https://crunchtimeodds.com) to get started and receive your API key via email for free. You can then login to your account dashboard to view and manage access to our products. The Crunchtime API uses API keys to authenticate requests. We authenticate your private API key using HTTP authorization request headers. Any request to authorized endpoints that doesn't include an API key will return an error.

Explore the [API documentation](https://crunchtimeodds.com/products/api/docs/overview) for more details.

## Setup

```bash
git clone https://github.com/crunchtimeodds/examples.git
cd examples
pip3 install -r requirements.txt
```

The `.env.example` file contains credentials, etc. needed to run code. Supply these values and rename `.env.example` to `.env` to get started.

## Run Live Odds

```bash
python3 explore.py
```

The `explore.py` script contains code for requesting endpoints and parsing moneyline, over under, and point spread odds response data. Visit the documentation for details on other endpoints and stats. Stay tuned for more examples coming soon!

Example console output from script:

```bash
[HEALTH] {'status': 'ok', 'version': '0.2.5'}
[TEAMS] 433 teams found
[SITES] 12 sites found
[GAME IDS] page = 0 | found 10 items
[GAME IDS] page = 1 | found 7 items
[GAME IDS] 17 game ids found in 2 pages
--------------------------------------------------
[ML ODDS UPDATE 2024-04-04 20:00:15] MLB | mlb-HoustonAstros-TexasRangers-1712361900 | OvertimeMarkets | Houston-Astros 1.7575757575757576 | Texas-Rangers 2.21
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Carolina-Washington-1712361600 | Betrivers | Carolina 1.4 | Washington 2.95
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Detroit-NYRangers-1712361600 | Betrivers | Detroit 2.14 | NY-Rangers 1.7092198581560283
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Buffalo-Philadelphia-1712361600 | Betrivers | Buffalo 1.8547008547008548 | Philadelphia 1.9433962264150944
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Colorado-Edmonton-1712361600 | Betrivers | Colorado 1.9433962264150944 | Edmonton 1.8547008547008548
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Anaheim-Seattle-1712361600 | Betrivers | Anaheim 2.2 | Seattle 1.6578947368421053
[ML ODDS UPDATE 2024-04-04 07:00:25] NHL | nhl-Vegas-Arizona-1712361600 | Betrivers | Vegas 1.5649717514124293 | Arizona 2.43
[ML ODDS UPDATE 2024-04-04 08:40:19] NHL | nhl-Vegas-Arizona-1712361600 | Betrivers | Vegas 1.598802395209581 | Arizona 2.35
--------------------------------------------------
[OU ODDS UPDATE 2024-04-04 20:00:15] MLB | mlb-LosAngelesAngels-BostonRedSox-1712367480 | OvertimeMarkets | over 2.0 | under 1.8333333333333333
[OU ODDS UPDATE 2024-04-04 21:40:11] MLB | mlb-LosAngelesAngels-BostonRedSox-1712367480 | OvertimeMarkets | over 1.8695652173913044 | under 1.9523809523809523
[OU ODDS UPDATE 2024-04-04 20:00:15] MLB | mlb-SeattleMariners-MilwaukeeBrewers-1712362200 | OvertimeMarkets | over 1.8333333333333333 | under 2.0
[OU ODDS UPDATE 2024-04-04 20:00:15] MLB | mlb-HoustonAstros-TexasRangers-1712361900 | OvertimeMarkets | over 1.9523809523809523 | under 1.8695652173913044
[OU ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Carolina-Washington-1712361600 | DraftKings | over 1.9090909090909092 | under 1.9090909090909092
[OU ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Detroit-NYRangers-1712361600 | DraftKings | over 1.9090909090909092 | under 1.9090909090909092
[OU ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Buffalo-Philadelphia-1712361600 | DraftKings | over 1.9523809523809523 | under 1.8695652173913044
[OU ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Colorado-Edmonton-1712361600 | DraftKings | over 2.0 | under 1.8333333333333333
--------------------------------------------------
[PS ODDS UPDATE 2024-04-04 20:00:15] MLB | mlb-HoustonAstros-TexasRangers-1712361900 | OvertimeMarkets | Houston-Astros 2.15 | Texas-Rangers 1.7407407407407407
[PS ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Carolina-Washington-1712361600 | DraftKings | Carolina 2.05 | Washington 1.8
[PS ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Detroit-NYRangers-1712361600 | DraftKings | Detroit 1.4587155963302751 | NY-Rangers 2.8
[PS ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Buffalo-Philadelphia-1712361600 | DraftKings | Buffalo 2.9 | Philadelphia 1.434782608695652
[PS ODDS UPDATE 2024-04-04 12:00:23] NHL | nhl-Colorado-Edmonton-1712361600 | DraftKings | Colorado 1.4444444444444444 | Edmonton 2.85
[PS ODDS UPDATE 2024-04-04 12:40:17] NHL | nhl-Carolina-Washington-1712361600 | Fanduel | Carolina 2.16 | Washington 1.7142857142857142
[PS ODDS UPDATE 2024-04-04 12:40:17] NHL | nhl-Detroit-NYRangers-1712361600 | Fanduel | Detroit 1.5 | NY-Rangers 2.64
[PS ODDS UPDATE 2024-04-04 12:40:17] NHL | nhl-Buffalo-Philadelphia-1712361600 | Fanduel | Buffalo 3.1 | Philadelphia 1.3846153846153846
--------------------------------------------------
```