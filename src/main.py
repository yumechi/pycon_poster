from janome.tokenizer import Tokenizer
from pathlib import Path
from wordcloud import WordCloud
import requests
import csv
from const import (
    GAS_URL,
    IGNORE_LIST_FILE,
    FILE_OUTPUT_DIR,
    EVENT_YEARS,
    LANGUAGE_STRING,
    TOPIC_NAMES,
    Language,
    ContentType,
    ContentJsonRow,
    JSON_COL,
    FONT_PATH,
)


def run() -> None:
    tokenizer = Tokenizer()
    ignore_list = set([])
    with open(IGNORE_LIST_FILE, "r") as f:
        ignore_list = set(f.readlines())

    topic_types_contents = {topic: {} for topic in TOPIC_NAMES}
    year_contents = {year: {} for year in EVENT_YEARS}
    for year in EVENT_YEARS:
        req = requests.get(GAS_URL, {"year": year})
        # まだデータを入れていない
        if year > 2012:
            break
        print(f"doing {year}")
        for content in req.json():
            if (
                content[JSON_COL[ContentJsonRow.LANGUAGE]]
                != LANGUAGE_STRING[Language.JA]
            ):
                continue
            for token in tokenizer.tokenize(content[JSON_COL[ContentJsonRow.CONTENT]]):
                if (
                    token.part_of_speech.split(",")[0] == "名詞"
                    and token.base_form not in ignore_list
                ):
                    normalized_name = token.base_form
                    year_contents[year][
                        content[JSON_COL[ContentJsonRow.CONTENT]]
                    ] = normalized_name
                    # 寄せてから
                    # topic_types_contents[year][
                    #     content[JSON_COL[ContentJsonRow.CONTENT]]
                    # ] = normalized_name

    wordcloud_outout = Path(FILE_OUTPUT_DIR)
    for year, content in year_contents.items():
        if not content:
            continue
        content_data = " ".join(content)
        wordcloud = WordCloud(font_path=FONT_PATH, width=600, height=400)
        wordcloud.generate(content_data)
        wordcloud_outout_year = wordcloud_outout / (str(year) + "_word_cloud.png")
        print(str(wordcloud_outout_year))
        wordcloud.to_file(str(wordcloud_outout_year))


if __name__ == "__main__":
    run()
