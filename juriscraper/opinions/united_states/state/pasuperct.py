"""
Scraper for Pennsylvania Superior Court
CourtID: pasup
Court Short Name: pasup
Author: Andrei Chelaru
Reviewer: mlr
Date created: 21 July 2014
"""

from datetime import datetime
from typing import Dict
from urllib.parse import urlencode

from juriscraper.opinions.united_states.state import pa


class Site(pa.Site):
    court = "Superior"
    days_interval = 20
    first_opinion_date = datetime(1998, 2, 15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.court_id = self.__module__
        self.params["postTypes"] = (
            "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,32,33"
        )
        self.url = f"{self.base_url}{urlencode(self.params)}"

    def get_status(self, op: Dict) -> str:
        """Get status from opinion object

        :param op: opinion json
        :return: parsed status
        """
        descr = op.get("PublicationType", {}).get("Description", "")
        if descr == "Non-Precedential":
            return "Unpublished"
        if descr == "Precedential":
            return "Published"
        return "Unknown"
