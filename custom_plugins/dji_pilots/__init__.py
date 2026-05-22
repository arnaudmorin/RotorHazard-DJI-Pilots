"""Pilot Prefered Band Selector."""

import logging

from eventmanager import Evt
from RHUI import UIField, UIFieldSelectOption, UIFieldType

logger = logging.getLogger(__name__)


class PilotPreferedBandSelector:
    """Pilot Prefered Band Selector."""

    def __init__(self, rhapi: any) -> None:
        """Init."""
        self._rhapi = rhapi
        self.enabled = True

    def initialize(self, _args: any) -> None:
        """Init wrapper."""
        logger.info("Initializing Pilot Prefered Band Selector")
        options = [
            UIFieldSelectOption("raceband", "RACEBAND"),
            UIFieldSelectOption("dji", "DJI"),
        ]
        self._rhapi.fields.register_pilot_attribute(
            UIField(
                "prefered_band",
                "Prefered Band",
                UIFieldType.SELECT,
                options=options,
                value="raceband",
            )
        )


def initialize(rhapi: any) -> None:
    """Init plugin."""
    s = PilotPreferedBandSelector(rhapi)
    rhapi.events.on(Evt.STARTUP, s.initialize)
