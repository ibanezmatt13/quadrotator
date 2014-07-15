quadrotator
===========

Simple GUI Yagi rotator for quadcopter FPV, tell's you where to point your Yagi, primitive.


This project is specific to NORB PCBs at this time. It is required that a NORB board or some device transmitting 600 baud RTTY in a particular format as per the UKHAS protocol, is operating on board the quadcopter.

The software reads in real time the data from dl-fldigi and parses to extract the current position of the quadcopter.

By referencing this position with that of the base receiving Yagi, the software will eventually provide an easy to use interface that tells you how to point the Yagi at any time.
