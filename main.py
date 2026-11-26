#!/usr/bin/env python3
"""Houseplant out-of-office auto-reply.

Prints the entry line to stdout; the make.fun harness captures stdout
into /output/entry.txt for the judge.

The line is 110 characters, inside the 120-character cap: the fern
ignored since March, rationing one sip of water, with the inbox queued
behind the dust.
"""

LINE = "Auto-reply: I've been rationing the same sip of water since March. Your email joins the queue behind the dust."

print(LINE)
