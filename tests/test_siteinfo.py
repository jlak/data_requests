#!/usr/bin/env python3

import logging
import unittest

from context import siteinfo

logging.basicConfig(level=logging.INFO)

INPUTS = {
    "good": "google.com",
    "unformatted": "htTPs://WWW.GoOgLe.COM",
    "bad": "https://www.badinput.com",
    "invalid": "invalidinput.invalidinput",
}

FUNCS = {
    "get_competitors": siteinfo.get_competitors,
    "get_similar_sites": siteinfo.get_similar_sites,
}


class TestGetCompetitors(unittest.TestCase):
    test = "get_competitors"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


class TestGetSimilarSites(unittest.TestCase):
    test = "get_similar_sites"

    def test_good_input(self):
        output = FUNCS[self.test](INPUTS["good"])
        self.assertTrue(len(output) > 0)

    def test_unformatted_input(self):
        output = FUNCS[self.test](INPUTS["unformatted"])
        self.assertTrue(len(output) > 0)

    def test_bad_input(self):
        output = FUNCS[self.test](INPUTS["bad"])
        self.assertEqual(output, None)

    def test_invalid_input(self):
        output = FUNCS[self.test](INPUTS["invalid"])
        self.assertEqual(output, None)


if __name__ == "__main__":
    unittest.main()
