# G5 TV Launcher — All features

[English](FEATURES.md) · [Deutsch](FEATURES.de.md) · [Back to README](README.md)

## Features

- Choose LG Home, the legacy method or Direct Home takeover under TV Home screen. Direct Home does not require Magic Mapper; the legacy method remains available. [Test and recovery](HOME_TAKEOVER_TEST.md).
- Optionally start the launcher with LG Home or the legacy method; turn it off before uninstalling. Direct Home uses its own startup mechanism.

- Browse, launch, hide, restore and reorder installed apps on Overview; HDMI inputs and Live TV have their own Inputs page.
- Add, remove and reorder favorites in the glass-style dock. Show app icons with or without names and choose from three icon sizes when names are hidden.
- Navigate using the Magic Remote directional controls, pointer and wheel.
- Open HDMI 1–4 and Live TV. HDMI names can be read from the TV's launch points or customized.
- Choose from eight illustrated scenes, including Halloween, Christmas and Cyberpunk under Special themes.
- With animations enabled, Halloween features a spider descending at changing positions, flickering house windows and a glowing pumpkin face. Christmas features falling snow and Santa's reindeer sleigh flying across the scene in alternating directions. The sleigh flies for 12 seconds with a 5-second pause; the effects can be switched off with animations.
- Show or hide the clock and weather independently, choose a digital or analog clock, and set a weather location.
- Select Overview, Favorites or Inputs as the start page, including when reopening the launcher.
- Switch the interface between English and German; English is the default.
- Optionally assign the Home button to this launcher using Magic Mapper 1.1.2, and restore the previous mapping. [Requirements and details](README.md#optional-home-button-mapping).
- Save and restore launcher settings, including favorites, app arrangement, imported themes and custom input labels, as a JSON backup on the TV.
- Search installed apps by name.
- Customize the three Overview shortcuts with apps, HDMI inputs or TV settings.
- Rotate backgrounds on each launch or according to the time of day.
- Enable or disable subtle page transitions and magnification of the focused favorite icon.
- Adjust favorite dock spacing, transparency and vertical position.
- Manually check the GitHub source for a newer version; the launcher does not install updates automatically.
- Adjust clock and weather sizes independently; set the weather refresh interval to 15 minutes, hourly, twice daily or daily.
- Choose Meteocons or Makin’ Things weather icons and independently enable or disable animation for each set. Day/night switching uses local sunrise and sunset times.
- Select Open-Meteo or GeoSphere Austria’s AROME model via Open-Meteo.
- Find weather locations in English and German, prefer a match in the TV's time zone, and choose among matching cities with region and country shown.
- Navigate settings by category to reduce scrolling.
- Browse backgrounds in separate Standard, Special and Imported theme categories.
- Import up to three custom JSON themes by selecting a matching file from the theme folder under /tmp or pasting JSON into the field. Select, update or remove imported themes. [Template and instructions](themes/README.md).
- Create imported theme scenes from shapes with individual motion, blinking and swaying; customize global effect color, duration, opacity and direction. [Template and guide](themes/README.md).
- Retry the weather request five seconds after launch, relaunch or return to the foreground.
- Experimental triple-Home recovery requires delivered Home relaunch events and is not an independent fallback when the interface is unresponsive.
