# menu/config.py
THEMES = {
    "github-dark": "Midnight Dark",
    "matrix-green": "Matrix Terminal"
}

LANGUAGES = {
    "en": "English (Global)", "es-ES": "Español (España)", "es-MX": "Español (México)", "es-AR": "Español (Argentina)", "es-CO": "Español (Colombia)",
    "fr-FR": "Français (France)", "fr-CA": "Français (Canada)", "fr-BE": "Français (Belgique)", "de-DE": "Deutsch (Deutschland)", "de-AT": "Deutsch (Österreich)",
    "de-CH": "Deutsch (Schweiz)", "it-IT": "Italiano (Italia)", "pt-BR": "Português (Brasil)", "pt-PT": "Português (Portugal)", "nl-NL": "Nederlands (Nederland)",
    "nl-BE": "Nederlands (België)", "ru-RU": "Русский (Россия)", "zh-CN": "简体中文 (中国)", "zh-TW": "繁體中文 (台灣)", "zh-HK": "繁體中文 (香港)",
    "ja-JP": "日本語 (日本)", "ko-KR": "한국어 (대한민국)", "hi-IN": "हिन्दी (भारत)", "bn-IN": "বাংলা (भारत)", "bn-BD": "বাংলা (বাংলাদেশ)",
    "te-IN": "తెలుగు (भारत)", "ta-IN": "தமிழ் (भारत)", "kn-IN": "ಕನ್ನಡ (भारत)", "mr-IN": "मराठी (भारत)", "gu-IN": "ગુજરાતી (भारत)",
    "pa-IN": "ಪ್ಲಾವಿ (भारत)", "ml-IN": "മലയാളം (भारत)", "or-IN": "ಒಡ଼ಿଆ (भारत)", "ur-PK": "اردو (پاکستان)", "ur-IN": "اردو (भारत)",
    "ar-SA": "العربية (السعودية)", "ar-EG": "العربية (مصر)", "ar-AE": "العربية (الإمارات)", "ar-MA": "العربية (المغرب)", "he-IL": "עברית (ישראל)",
    "tr-TR": "Türkçe (Türkiye)", "vi-VN": "Tiếng Việt (Việt Nam)", "th-TH": "ไทย (ประเทศไทย)", "id-ID": "Bahasa Indonesia (Indonesia)", "ms-MY": "Bahasa Melayu (Malaysia)",
    "fil-PH": "Filipino (Pilipinas)", "pl-PL": "Polski (Polska)", "uk-UA": "Українська (Україна)", "ro-RO": "Română (România)", "cs-CZ": "Čeština (Česko)",
    "el-GR": "Ελληνικά (Ελλάδα)", "hu-HU": "Magyar (Magyarország)", "sv-SE": "Svenska (Sverige)", "no-NO": "Norsk (Norge)", "da-DK": "Dansk (Danmark)",
    "fi-FI": "Suomi (Suomi)", "cs-SK": "Slovenčina (Slovensko)", "bg-BG": "Български (България)", "hr-HR": "Hrvatski (Hrvatska)", "sr-RS": "Srpski (Srbija)",
    "sl-SI": "Slovenščina (Slovenija)", "et-EE": "Eesti (Eesti)", "lv-LV": "Latviešu (Latvija)", "lt-LT": "Lietuvių (Lietuva)", "fa-IR": "فارسی (ایران)",
    "sw-KE": "Kiswahili (Kenya)", "sw-TZ": "Kiswahili (Tanzania)", "am-ET": "አማርኛ (ኢትዮጵያ)", "az-AZ": "Azərbaycanca (Azərbaycan)", "ka-GE": "Ქართული (საქართველო)",
    "hy-AM": "Հայերեն (Հայաստան)", "uz-UZ": "Oʻzbekcha (Oʻzbekiston)", "kk-KZ": "Қαзақ тілі (Қαзақستان)", "ky-KG": "Кыргызಚಾ (Кыргызستان)", "tg-TJ": "Тоҷикӣ (Тоҷикистон)",
    "tk-TM": "Türkmençe (Türkmenistan)", "mn-MN": "Мονгол (Монгол улс)", "km-KH": "ខ្មែរ (កម្ពុជា)", "lo-LA": "ឡಾವ (លាវ)", "my-MM": "မြန်မာ (မြန်မာ)",
    "ne-NP": "नेपाली (नेपाल)", "si-LK": "ಸಿಂಹಲ (ශ್ರೀ ลංකා)", "si-LK-en": "Sinhala (Sri Lanka)", "af-ZA": "Afrikaans (Suid-Afrika)", "zu-ZA": "isiZulu (Suid-Afrika)",
    "xh-ZA": "isiXhosa (Suid-Afrika)", "tn-ZA": "Setswana (Suid-Afrika)", "st-LS": "Sesotho (Lesotho)", "ss-SZ": "SiSwati (Eswatini)", "nr-ZA": "isiNdebele (Suid-Afrika)",
    "ts-ZA": "Xitsonga (Suid-Afrika)", "ve-ZA": "Tshivenda (Suid-Afrika)", "sq-AL": "Shqip (Shqipëria)", "mk-MK": "Македонски (Македонија)", "bs-BA": "Bosanski (Bosna i Hercegovina)",
    "cy-GB": "Cymraeg (Cymru)", "ga-IE": "Gaeilge (Éire)", "gd-GB": "Gàidhlig (Alba)", "kw-GB": "Kernewek (Cornwall)", "gl-ES": "Galego (Galicia)",
    "eu-ES": "Euskara (Euskal Herria)", "ca-ES": "Català (Catalunya)", "is-IS": "Íslenska (Ísland)", "mt-MT": "Malti (Malta)", "lb-LU": "Lëtzebuergesch (Lëtzebuerg)",
    "fy-NL": "Frysk (Fryslân)", "wa-BE": "Walon (Wallonreye)", "br-FR": "Brezhoneg (Breizh)", "co-FR": "Corsu (Corsica)", "fo-FO": "Føroyskt (Føroyar)",
    "kl-GL": "Kalaallisut (Greenland)", "haw-US": "Hawaiian (Hawaiʻi)", "mi-NZ": "Māori (New Zealand)", "sm-WS": "Gagana Sāmoa (Samoa)", "to-TO": "Faka-Tonga (Tonga)",
    "fj-FJ": "Na Vosa Vakaviti (Fiji)", "bi-VU": "Bislama (Vanuatu)", "ch-GU": "Chamoru (Guam)", "mh-MH": "Kajin M̧ajeļ (Marshall Islands)", "tv-TV": "Tuvalu (Tuvalu)",
    "na-NR": "Dorerin Naoero (Nauru)", "ho-PG": "Hiri Motu (Papua New Guinea)", "tpi-PG": "Tok Pisin (Papua New Guinea)", "ay-BO": "Aymar aru (Bolivia)", "qu-PE": "Runa Simi (Perú)",
    "gn-PY": "Avañe'ẽ (Paraguay)", "sm-AS": "Samoan (American Samoa)", "so-SO": "Af-Soomaali (Somalia)", "ti-ER": "ትግርኛ (Eritrea)", "rw-RW": "Ikinyarwanda (Rwanda)",
    "rn-BI": "Ikirundi (Burundi)", "yo-NG": "Yorùbá (Nàìjíríà)", "ig-NG": "Asụsụ Igbo (Nàìjíríà)", "ha-NG": "Hausa (Nigeria)", "ak-GH": "Akan (Ghana)"
}

DEFAULT_SETTINGS = {
    "account_display_name": "Guest Operator",
    "avatar_emoji": "🚀",
    "selected_theme": "github-dark",
    "selected_language": "en",
    "auth_type": "guest"
}