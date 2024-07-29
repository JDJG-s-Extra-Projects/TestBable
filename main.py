import datetime
import zoneinfo

import discord
from babel import Locale
from babel.dates import get_timezone_name

timezones = list(zoneinfo.available_timezones())


for locale in discord.Locale:
    with open(
        f"test/locales/{locale.value}.txt",
        "w",
    ) as f:
        for timezone in timezones:
            cleaned_locale = locale.value.replace(
                "-",
                "_",
            )
            try:
                localized_datetime = datetime.datetime.now(tz=zoneinfo.ZoneInfo(timezone))
                timezone_localized = get_timezone_name(
                    localized_datetime,
                    locale=Locale.parse(cleaned_locale),
                )
                if timezone_localized.lower().startswith("unknown region"):
                    timezone_localized = timezone

                f.write(f"{timezone_localized}: {timezone}")
                f.write("\n")

            except LookupError:
                pass

print("complete")
