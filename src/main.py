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
        ignore_list = set([line.strip() for line in f.readlines()])

    topic_types_contents = {topic: {} for topic in TOPIC_NAMES}
    year_contents = {year: {} for year in EVENT_YEARS}
    for year in EVENT_YEARS:
        req = requests.get(GAS_URL, {"year": year})
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
                    and len(token.base_form) > 1
                ):
                    normalized_name = token.base_form
                    if not year_contents[year].get(
                        content[JSON_COL[ContentJsonRow.TOPIC_TYPE]]
                    ):
                        year_contents[year][
                            content[JSON_COL[ContentJsonRow.TOPIC_TYPE]]
                        ] = []
                    year_contents[year][
                        content[JSON_COL[ContentJsonRow.TOPIC_TYPE]]
                    ].append(normalized_name)
                    # 寄せてから
                    # topic_types_contents[year][
                    #     content[JSON_COL[ContentJsonRow.CONTENT]]
                    # ] = normalized_name

    wordcloud_outout_dir = Path(FILE_OUTPUT_DIR)
    for year, contents in year_contents.items():
        if not contents:
            continue
        year_content_data = []
        for topic, inner_content in contents.items():
            if not inner_content:
                continue
            content_data = " ".join(inner_content)
            year_content_data.append(content_data)
            # wordcloud = WordCloud(font_path=FONT_PATH, width=600, height=400)
            # wordcloud.generate(content_data)
            # wordcloud_outout_file = wordcloud_outout_dir / (
            #     f"{year}_{topic}_word_cloud.png"
            # )
            # print(str(wordcloud_outout_file))
            # wordcloud.to_file(str(wordcloud_outout_file))

        content_data = " ".join(year_content_data)
        print("year: ", content_data)
        wordcloud = WordCloud(font_path=FONT_PATH, background_color='white', width=600, height=400)
        wordcloud.generate(content_data)
        wordcloud_outout_file = wordcloud_outout_dir / (f"{year}_word_cloud.png")
        print(str(wordcloud_outout_file))
        wordcloud.to_file(str(wordcloud_outout_file))


if __name__ == "__main__":
    run()
