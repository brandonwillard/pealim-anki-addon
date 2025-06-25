from typing import List, NamedTuple
from bs4 import BeautifulSoup as bs
import requests
import unicodedata

# from jinja2 import Environment, FileSystemLoader
# from pathlib import Path

# templates_dir = Path(__file__).parent
# templates_dir = templates_dir.absolute()
# env = Environment(loader=FileSystemLoader(templates_dir))
# template = env.get_template("verb_he_en.html")

pealim_to_jinja = {
    "AP-ms": "p_x_s_m",
    "AP-fs": "p_x_s_f",
    "AP-mp": "p_x_p_m",
    "AP-fp": "p_x_p_f",
    "PERF-1s": "pp_1_s_x",
    "PERF-1p": "pp_1_p_x",
    "PERF-2ms": "pp_2_s_m",
    "PERF-2fs": "pp_2_s_f",
    "PERF-2mp": "pp_2_p_m",
    "PERF-2fp": "pp_2_p_f",
    "PERF-3ms": "pp_3_s_m",
    "PERF-3fs": "pp_3_s_f",
    "PERF-3p": "pp_3_p_x",
    "IMPF-1s": "f_1_s_x",
    "IMPF-1p": "f_1_p_x",
    "IMPF-2ms": "f_2_s_m",
    "IMPF-2fs": "f_2_s_f",
    "IMPF-2mp": "f_2_p_m",
    "IMPF-2fp": "f_2_p_f",
    "IMPF-3ms": "f_3_s_m",
    "IMPF-3fs": "f_3_s_f",
    "IMPF-3mp": "f_3_p_m",
    "IMPF-3fp": "f_3_p_f",
    "IMP-2ms": "im_2_s_m",
    "IMP-2fs": "im_2_s_f",
    "IMP-2mp": "im_2_p_m",
    "IMP-2fp": "im_2_p_f",
    "INF-L": "inf",
}


class HebrewBasic(NamedTuple):
    Hebrew: str
    HebrewCheck: str
    English: str
    EnglishCheck: str
    Note: str
    tags: List[str]


class HebrewAdjectiveConjugation(NamedTuple):
    FirstSecondThirdPersonSingularMaleHebrew: str
    FirstSecondThirdPersonSingularMaleHebrewCheck: str
    FirstSecondThirdPersonSingularMaleEnglish: str
    FirstSecondThirdPersonSingularFemaleHebrew: str
    FirstSecondThirdPersonSingularFemaleHebrewCheck: str
    FirstSecondThirdPersonSingularFemaleEnglish: str
    FirstSecondThirdPersonPluralMaleHebrew: str
    FirstSecondThirdPersonPluralMaleHebrewCheck: str
    FirstSecondThirdPersonPluralMaleEnglish: str
    FirstSecondThirdPersonPluralFemaleHebrew: str
    FirstSecondThirdPersonPluralFemaleHebrewCheck: str
    FirstSecondThirdPersonPluralFemaleEnglish: str
    Note: str
    tags: List[str]


class HebrewNoun(NamedTuple):
    SingularHebrew: str
    SingularHebrewCheck: str
    SingularEnglish: str
    SingularEnglishCheck: str
    PluralHebrew: str
    PluralHebrewCheck: str
    PluralEnglish: str
    PluralEnglishCheck: str
    Note: str
    tags: List[str]


class HebrewFutureTenseConjugation(NamedTuple):
    FirstPersonSingularHebrew: str
    FirstPersonSingularHebrewCheck: str
    FirstPersonSingularEnglish: str
    SecondPersonSingularMaleHebrew: str
    SecondPersonSingularMaleHebrewCheck: str
    SecondPersonSingularMaleEnglish: str
    SecondPersonSingularFemaleHebrew: str
    SecondPersonSingularFemaleHebrewCheck: str
    SecondPersonSingularFemaleEnglish: str
    ThirdPersonSingularMaleHebrew: str
    ThirdPersonSingularMaleHebrewCheck: str
    ThirdPersonSingularMaleEnglish: str
    ThirdPersonSingularFemaleHebrew: str
    ThirdPersonSingularFemaleHebrewCheck: str
    ThirdPersonSingularFemaleEnglish: str
    FirstPersonPluralHebrew: str
    FirstPersonPluralHebrewCheck: str
    FirstPersonPluralEnglish: str
    SecondPersonPluralMaleHebrew: str
    SecondPersonPluralMaleHebrewCheck: str
    SecondPersonPluralMaleEnglish: str
    SecondPersonPluralFemaleHebrew: str
    SecondPersonPluralFemaleHebrewCheck: str
    SecondPersonPluralFemaleEnglish: str
    ThirdPersonPluralMaleHebrew: str
    ThirdPersonPluralMaleHebrewCheck: str
    ThirdPersonPluralMaleEnglish: str
    ThirdPersonPluralFemaleHebrew: str
    ThirdPersonPluralFemaleHebrewCheck: str
    ThirdPersonPluralFemaleEnglish: str
    Note: str
    tags: List[str]


class HebrewImperativeConjugation(NamedTuple):
    SecondPersonSingularMaleHebrew: str
    SecondPersonSingularMaleHebrewCheck: str
    SecondPersonSingularMaleEnglish: str
    SecondPersonSingularFemaleHebrew: str
    SecondPersonSingularFemaleHebrewCheck: str
    SecondPersonSingularFemaleEnglish: str
    SecondPersonPluralMaleHebrew: str
    SecondPersonPluralMaleHebrewCheck: str
    SecondPersonPluralMaleEnglish: str
    SecondPersonPluralFemaleHebrew: str
    SecondPersonPluralFemaleHebrewCheck: str
    SecondPersonPluralFemaleEnglish: str
    Note: str
    tags: List[str]


class HebrewPastTenseConjugation(NamedTuple):
    FirstPersonSingularHebrew: str
    FirstPersonSingularHebrewCheck: str
    FirstPersonSingularEnglish: str
    SecondPersonSingularMaleHebrew: str
    SecondPersonSingularMaleHebrewCheck: str
    SecondPersonSingularMaleEnglish: str
    SecondPersonSingularFemaleHebrew: str
    SecondPersonSingularFemaleHebrewCheck: str
    SecondPersonSingularFemaleEnglish: str
    ThirdPersonSingularMaleHebrew: str
    ThirdPersonSingularMaleHebrewCheck: str
    ThirdPersonSingularMaleEnglish: str
    ThirdPersonSingularFemaleHebrew: str
    ThirdPersonSingularFemaleHebrewCheck: str
    ThirdPersonSingularFemaleEnglish: str
    FirstPersonPluralHebrew: str
    FirstPersonPluralHebrewCheck: str
    FirstPersonPluralEnglish: str
    SecondPersonPluralMaleHebrew: str
    SecondPersonPluralMaleHebrewCheck: str
    SecondPersonPluralMaleEnglish: str
    SecondPersonPluralFemaleHebrew: str
    SecondPersonPluralFemaleHebrewCheck: str
    SecondPersonPluralFemaleEnglish: str
    ThirdPersonPluralHebrew: str
    ThirdPersonPluralHebrewCheck: str
    ThirdPersonPluralEnglish: str
    Note: str
    tags: List[str]


class HebrewPresentTenseConjugation(NamedTuple):
    FirstSecondThirdPersonSingularMaleHebrew: str
    FirstSecondThirdPersonSingularMaleHebrewCheck: str
    FirstSecondThirdPersonSingularMaleEnglish: str
    FirstSecondThirdPersonSingularFemaleHebrew: str
    FirstSecondThirdPersonSingularFemaleHebrewCheck: str
    FirstSecondThirdPersonSingularFemaleEnglish: str
    FirstSecondThirdPersonPluralMaleHebrew: str
    FirstSecondThirdPersonPluralMaleHebrewCheck: str
    FirstSecondThirdPersonPluralMaleEnglish: str
    FirstSecondThirdPersonPluralFemaleHebrew: str
    FirstSecondThirdPersonPluralFemaleHebrewCheck: str
    FirstSecondThirdPersonPluralFemaleEnglish: str
    Note: str
    tags: List[str]


def convert_shoresh(shoresh: str) -> str:
    if not shoresh:
        return

    shoresh = shoresh.replace(" ", "").split("-")

    tags = []
    if len(shoresh) == 3:
        if shoresh[0] == "א":
            tags += ["פ''א"]
        elif shoresh[0] == "ע":
            tags += ["פ''ע"]
        elif shoresh[0] == "ה":
            tags += ["פ''ה"]
        elif shoresh[0] == "ח":
            tags += ["פ''ח"]
        elif shoresh[0] == "י":
            tags += ["פ''י"]
        elif shoresh[0] == "נ":
            tags += ["פ''נ"]

        if shoresh[1] == "א":
            tags += ["ע''א"]
        elif shoresh[1] == "ע":
            tags += ["ע''ע"]
        elif shoresh[1] == "ה":
            tags += ["ע''ה"]
        elif shoresh[1] == "ח":
            tags += ["ע''ח"]
        elif shoresh[1] == "ו":
            tags += ["ע''ו"]
        elif shoresh[1] == "י":
            tags += ["ע''י"]
        elif shoresh[1] == "ר":
            tags += ["ע''ר"]

        if shoresh[2] == "א":
            tags += ["ל''א"]
        elif shoresh[2] == "ע":
            tags += ["ל''ע"]
        elif shoresh[2] == "ה":
            tags += ["ל''ה"]
        elif shoresh[2] == "ח":
            tags += ["ל''ח"]

    return tags


def extract_binyan(text: str):
    upper = text.upper()
    if "PA'AL" in upper:
        return "פָּעַל"
    elif "PI'EL" in upper:
        return "פִּעֵל"
    elif "HIF'IL" in upper:
        return "הִפְעִיל"
    elif "HITPA'EL" in upper:
        return "הִתְפַּעֵל"
    elif "NIF'AL" in upper:
        return "נִפְעַל"
    elif "PU'AL" in upper:
        return "פֻּעַל"
    elif "HUF'AL" in upper:
        return "הֻפְעַל"
    else:
        return ""


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def convert_verb(soup):
    out_dict = {}

    shoresh = soup.find("span", class_="menukad").text
    # definition = soup.find("div", class_="lead").text

    tags = []

    for peal, jinj in pealim_to_jinja.items():
        div = soup.find("div", id=peal)
        word = div.find("span", class_="menukad").text
        # pron = div.find("div", class_="transcription").text
        meaning = div.find("div", class_="meaning").text

        if peal.startswith("IMP"):
            word = word.strip("!\u200f")

        word_and_stripped = (word, strip_accents(word), meaning)

        out_dict[jinj] = word_and_stripped

    binyan_p = get_subheader(soup)
    binyan = extract_binyan(binyan_p)

    paal_tags = convert_shoresh(shoresh)

    inf_card = HebrewBasic(
        *out_dict["inf"],
        "",
        "",
        ["infinitive", binyan] + paal_tags,
    )
    present_card = HebrewPresentTenseConjugation(
        *out_dict["p_x_s_m"],
        *out_dict["p_x_s_f"],
        *out_dict["p_x_p_m"],
        *out_dict["p_x_p_f"],
        "",
        ["הוה", binyan] + paal_tags,
    )
    past_card = HebrewPastTenseConjugation(
        *out_dict["pp_1_s_x"],
        *out_dict["pp_2_s_m"],
        *out_dict["pp_2_s_f"],
        *out_dict["pp_3_s_m"],
        *out_dict["pp_3_s_f"],
        *out_dict["pp_1_p_x"],
        *out_dict["pp_2_p_m"],
        *out_dict["pp_2_p_f"],
        *out_dict["pp_3_p_x"],
        "",
        ["עבר", binyan] + paal_tags,
    )
    future_card = HebrewFutureTenseConjugation(
        *out_dict["f_1_s_x"],
        *out_dict["f_2_s_m"],
        *out_dict["f_2_s_f"],
        *out_dict["f_3_s_m"],
        *out_dict["f_3_s_f"],
        *out_dict["f_1_p_x"],
        *out_dict["f_2_p_m"],
        *out_dict["f_2_p_f"],
        *out_dict["f_3_p_m"],
        *out_dict["f_3_p_f"],
        "",
        ["עתיד", binyan] + paal_tags,
    )
    imp_card = HebrewImperativeConjugation(
        *out_dict["im_2_s_m"],
        *out_dict["im_2_s_f"],
        *out_dict["im_2_p_m"],
        *out_dict["im_2_p_f"],
        "",
        ["צווי", binyan] + paal_tags,
    )

    tags += [binyan]

    results = {
        "Hebrew Basic and Reversed Type-in": inf_card,
        "Hebrew Present Tense Conjugation": present_card,
        "Hebrew Past Tense Conjugation": past_card,
        "Hebrew Future Tense Conjugation": future_card,
        "Hebrew Imperative Conjugation": imp_card,
    }

    return results


def convert_noun(soup):
    # shoresh = None
    # for p in soup.find_all("p"):
    #     if p.text.startswith("Root:"):
    #         shoresh = p.find("span").text
    #
    # definition = soup.find("div", class_="lead").text

    t1 = soup.find("table", class_="conjugation-table")

    singular = t1.find("div", id="s").find("span", class_="menukad").text
    # singular_pr = t1.find("div", id="s").find("div", class_="transcription").text
    singular_meaning = t1.find("div", id="s").find("div", class_="meaning").text

    plural_div = t1.find("div", id="p")
    plural, plural_meaning = "", ""
    if plural_div is not None:
        plural = plural_div.find("span", class_="menukad").text
        # plural_pr = plural_div.find("div", class_="transcription").text
        plural_meaning = plural_div.find("div", class_="meaning").text

    gender = None
    for p in soup.find_all("p"):
        if p.text.startswith("Noun"):
            gender_field = p.text.split(" ")[-1]
            gender = "נקבה" if "fem" in gender_field else ""
            gender = "זכר" if "mas" in gender_field else ""

    results = {
        "Hebrew Noun Reversed Type-in": HebrewNoun(
            singular,
            strip_accents(singular),
            singular_meaning,
            "",
            plural,
            strip_accents(plural),
            plural_meaning,
            "",
            "",
            [gender],
        )
    }

    return results


def convert_adj(soup):
    # shoresh = None
    # for p in soup.find_all("p"):
    #     if p.text.startswith("Root:"):
    #         shoresh = p.find("span").text
    #
    # definition = soup.find("div", class_="lead").text

    t1 = soup.find("table", class_="conjugation-table")

    m_singular = t1.find("div", id="ms-a").find("span", class_="menukad").parent.text
    # m_singular_pr = t1.find("div", id="ms-a").find("div", class_="transcription").text
    m_singular_meaning = t1.find("div", id="ms-a").find("div", class_="meaning").text
    m_plural = t1.find("div", id="mp-a").find("span", class_="menukad").parent.text
    # m_plural_pr = t1.find("div", id="mp-a").find("div", class_="transcription").text
    m_plural_meaning = t1.find("div", id="mp-a").find("div", class_="meaning").text

    f_singular = t1.find("div", id="fs-a").find("span", class_="menukad").parent.text
    # f_singular_pr = t1.find("div", id="fs-a").find("div", class_="transcription").text
    f_singular_meaning = t1.find("div", id="fs-a").find("div", class_="meaning").text
    f_plural = t1.find("div", id="fp-a").find("span", class_="menukad").parent.text
    # f_plural_pr = t1.find("div", id="fp-a").find("div", class_="transcription").text
    f_plural_meaning = t1.find("div", id="fp-a").find("div", class_="meaning").text

    results = {
        "Hebrew Adjective Conjugation": HebrewAdjectiveConjugation(
            m_singular,
            strip_accents(m_singular),
            m_singular_meaning,
            f_singular,
            strip_accents(f_singular),
            f_singular_meaning,
            m_plural,
            strip_accents(m_plural),
            m_plural_meaning,
            f_plural,
            strip_accents(f_plural),
            f_plural_meaning,
            "",
            ["adjective"],
        )
    }

    return results


def extract_pos(text: str):
    if "noun" in text.lower():
        return convert_noun
    if "verb" in text.lower():
        return convert_verb
    if "adjective" in text.lower():
        return convert_adj


def get_subheader(soup) -> str:
    return soup.find("h2", class_="page-header").next_sibling.text


def translate(url) -> List[str]:
    resp = requests.get(url)
    soup = bs(resp.content, features="html.parser")

    pos_p = get_subheader(soup)
    fun = extract_pos(pos_p)

    return fun(soup)


# translate("https://www.pealim.com/dict/55-lomar/")
# translate("https://www.pealim.com/dict/8387-amir/")
# translate("https://www.pealim.com/dict/3801-amur/")
