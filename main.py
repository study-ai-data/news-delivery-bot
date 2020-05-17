import sys
import datetime
from github import Github, Issue
from pytz import timezone
from dateutil.parser import parse

from yonhap import Yonhap


if __name__ == "__main__":
    """ init setting """
    yonhap = Yonhap()

    """ crawling news data"""
    yonhap.crawling()
