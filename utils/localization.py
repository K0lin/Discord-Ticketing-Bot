# Copyright (c) 2025 K0lin
# This code is subject to the terms of the Custom Restricted License.
# See LICENSE.md for details.


"""
Handling the localization and multi-translator support through dictionaries in json format in the ../lang directory.
"""

#External Library
import json
import sys
from typing import List, Dict
#local file
from utils.paths_manager import PathsManager
from utils.config_manager import ConfigManager


class Translator:
    """
    Handles the translator of ui elements and strings. The class is a singleton to ensure there's only one instance in
    the app life-cycle.
    """

    _instance = None # Only one Translator instance

    def __new__(cls, lang_code="en", , configManager = None):
        """
        Ensures that only one instance of Translator is created (Singleton pattern).
        Initializes the translator code and loads the translations.

        :param lang_code: The translator code for the translation file (default is "en").
        :return: A single instance of the Translator class.
        """
        if not cls._instance:
            cls._instance = super(Translator,cls).__new__(cls)
            cls._instance.lang_code = lang_code
            cls._instance.configManager = configManager
            cls._instance.translations = cls._instance.load_translations()
        return cls._instance

    def load_translations(self) -> Dict[str,str]:
        """
        Loads all translation key-value pairs from the JSON dictionary for the specified translator.

        :return: A dictionary containing translation keys and their corresponding translated values.
        :raises FileNotFoundError: If the translation file for the given translator does not exist.
        """
        lang_code = self.lang_code
        log_enabled = self.configManager.getConsoleLogEnabled()
        try:
            abs_path = PathsManager.get_root_absolute_path()
            with open(f"{abs_path}/lang/{lang_code}.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            if log_enabled:
                print(f"Language dictionary {lang_code}.json was not found. Will use the default translator (English).")
                try:
                    with open(f"{abs_path}/lang/en.json", "r", encoding="utf-8") as f:
                        return json.load(f)
                except FileNotFoundError:
                    if log_enabled:
                        print(f"Default translator (lang/en.json) was not found. Terminating the program.")
                        sys.exit(1)

    def translate(self,key:str,**kwargs) -> str:
        """
        Translates a given key from the JSON dictionary and replaces any placeholders with values.

        :param key: The key of the translation to fetch.
        :param kwargs: Additional placeholders in the string that need to be replaced.
        :return: The translated string, with placeholders replaced by the provided values.
        """
        template = self.translations.get(key, f"[Missing:{key}]")
        return template.format(**kwargs)
