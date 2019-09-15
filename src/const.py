from enum import Enum

GAS_URL = "https://script.google.com/macros/s/AKfycbwMLo1rimAtKtKAelMtwjj2xNhm_nfp1jOWhTfa8XqfaTF0k4w/exec"
EVENT_YEARS = (
    2011,
    2012,  # 概要が短いので利用しないほうがいいかも
    2013,  # 概要が短いので利用しないほうがいいかも
    2014,
    # 2015, # 使用しない、現在サイト側で公開されていない
    2016,
    2017,
    # 2018, # なんかタグ付が違う
)

TOPIC_NAMES = (
    "Machine learning and data science",
    "Fintech",
    "Web programming, including frameworks(i.e Django, Flask, Pylons etc.)",
    "System administration",
    "Python libraries, extending and embedding python in hardware",
    "Python in education, science and maths",
    "GUI and games",
    "Network programming",
    "Packaging",
    "Programming tools",
    "Project case studies",
    "Best practices",
    "Community building and human interaction",
    "Business efficiency solution",
    "Anything else basically which doesn’t really fall into the types of topics above",
)

IGNORE_LIST_FILE = "./ignore_list.txt"
FILE_OUTPUT_DIR = "./wordcloud_img/"
# mkdir fonts && cd fonts && curl -o notosans.zip https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip && unzip notosans.zip && cd ..
FONT_PATH = "./fonts/NotoSansCJKjp-Medium.otf"


class Language(Enum):
    JA = 1
    EN = 2
    OTHER = 3


LANGUAGE_STRING = {Language.JA: "ja", Language.EN: "en", Language.OTHER: "other"}


class ContentType(Enum):
    MACHINE_LEARNING_AND_DATA_SCIENCE = 1
    FINTECH = 2
    WEB = 3
    SYSTEM_ADMINISTRATION = 4
    PYTHON_LIB_AND_EMBED_HARDWARE = 5
    EDUCATION = 6
    GUI_AND_GAMES = 7
    NETWORK = 8
    PACKAGING = 9
    PROGRAMMING_TOOLS = 10
    PROJECT_CASE_STUDIES = 11
    BEST_PRACTICES = 12
    COMMUNITY_BUILDING_AND_HUMAN_INTERRACTION = 13
    BUSINESS = 14
    OTHERS = 15


class ContentJsonRow(Enum):
    LANGUAGE = 1
    TOPIC_TYPE = 2
    CONTENT = 3


JSON_COL = {
    ContentJsonRow.LANGUAGE: "language",
    ContentJsonRow.TOPIC_TYPE: "topic_type",
    ContentJsonRow.CONTENT: "content",
}
